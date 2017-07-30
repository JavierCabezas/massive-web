<?php namespace app\module\api\controllers;
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 7/30/17
 * Time: 12:16 PM
 */
use Yii;
use yii\web\Response;
use yii\filters\auth\HttpBearerAuth;
use yii\rest\Controller;

class UserController extends Controller
{

    public function behaviors()
    {
        $behaviors = parent::behaviors();
        $behaviors['authenticator'] = [
            'class' => HttpBearerAuth::className(),
            'except' => ['login', 'register'],
        ];

        return $behaviors;
    }

    public function actionList()
    {
        Yii::$app->response->format = Response::FORMAT_JSON;
        return ['a' => 'b'];
    }
}