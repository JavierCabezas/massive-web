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

                if(!UserGoogleLoginTrait::verify($user_data['token'])){
                    throw new UnauthorizedHttpException();
                }else{
                    return 'Todo oK';
                }

                break;
        }

    }
}