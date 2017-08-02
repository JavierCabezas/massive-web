<?php namespace app\module\api\controllers;
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 7/30/17
 * Time: 12:16 PM
 */
use app\models\Login\User;
use app\models\Razgo\UserGoogleLoginTrait;
use Yii;
use yii\web\Response;
use yii\filters\{VerbFilter, auth\HttpBearerAuth};
use yii\rest\Controller;
use yii\web\UnauthorizedHttpException;

class UserController extends Controller
{

    public function behaviors()
    {
        $behaviors = parent::behaviors();
        $behaviors['authenticator'] = [
            'class' => HttpBearerAuth::className(),
            'except' => [ 'login' ],
        ];
        $behaviors['verbs'] = [
            'class' => VerbFilter::className(),
            'actions' => [
                'login' => ['post'],
                'profile-data' => ['get']
            ],
        ];

        return $behaviors;
    }

    /**
     * Logins an user
     * If the user is not yet created it creates it first and then does the login.
     * @return array
     */
    public function actionLogin()
    {
        Yii::$app->response->format = Response::FORMAT_JSON;

        $type = $_POST['type'];
        $user_data = $_POST['user_data'];

        switch($type){
            case 'google':
                $google_response = UserGoogleLoginTrait::verify($user_data['token']);
                if(!$google_response){
                    throw new UnauthorizedHttpException();
                }
                $user = User::find()->where(['email' => $google_response['email']])->one();
                if(!$user){
                    $user = User::createGoogleUser($google_response, $user_data);
                }
                if(!$user){
                    throw new \yii\web\HttpException(500, 'An error occured while creating the user');
                }

                return $user->token;
        }
    }

    public function actionProfileData()
    {
        Yii::$app->response->format = Response::FORMAT_JSON;
        $user = Yii::$app->user->identity;
        if ($user) {
            return $user->backendData;
        }
        throw new UnauthorizedHttpException('Usuario No Encontrado');
    }
}