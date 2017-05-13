<?php

namespace app\controllers;

use Yii;
use yii\filters\AccessControl;
use yii\web\Controller;
use yii\web\Response;
use yii\filters\VerbFilter;

class SiteController extends Controller
{
    /**
     * @inheritdoc
     */
    public function behaviors()
    {
        return [
            'access' => [
                'class' => AccessControl::className(),
                'only' => ['logout'],
                'rules' => [
                    [
                        'actions' => ['logout'],
                        'allow' => true,
                        'roles' => ['@'],
                    ],
                ],
            ],
            'verbs' => [
                'class' => VerbFilter::className(),
                'actions' => [
                    'logout' => ['post'],
                ],
            ],
        ];
    }

    /**
     * @inheritdoc
     */
    public function actions()
    {
        return [
            'error' => [
                'class' => 'yii\web\ErrorAction',
            ],
            'captcha' => [
                'class' => 'yii\captcha\CaptchaAction',
                'fixedVerifyCode' => YII_ENV_TEST ? 'testme' : null,
            ],
        ];
    }

    /**
     * Displays homepage.
     *
     * @return string
     */
    public function actionIndex()
    {
        return $this->render('index');
    }

    /**
     * Login action.
     *
     * @return Response|string
     */
    public function actionLogin()
    {
        if (!Yii::$app->user->isGuest) {
            return $this->goHome();
        }

        $model = new LoginForm();
        if ($model->load(Yii::$app->request->post()) && $model->login()) {
            return $this->goBack();
        }
        return $this->render('login', [
            'model' => $model,
        ]);
    }

    /**
     * Logout action.
     *
     * @return Response
     */
    public function actionLogout()
    {
        Yii::$app->user->logout();

        return $this->goHome();
    }

    public function actionMusicPacks(){
        Yii::$app->response->format = Response::FORMAT_JSON;

        $titles = [ "Four loko", "Fixie nostrud", "Master Cleanse", "Scenester hell", "Shabby chic", "Blue bottle", "Duis pitchfork", "Raclette portland", "Cardigan glossier", "Tumeric keffiyeh" ];
        $text = [
            "90's slow-carb twee everyday carry vegan aliquip, chambray affogato. Listicle enim hella, master cleanse cold-pressed YOLO hammock snackwave lumbersexual VHS. ",
            "Hexagon meditation elit, banh mi chambray sriracha qui tote bag. Poke delectus sustainable next level cred dolore mumblecore. Activated charcoal tbh hot chicken, pok pok yuccie man braid craft beer",
            "Duis pitchfork before they sold out yr. Yuccie deserunt delectus incididunt, raclette lumbersexual et VHS laborum freegan cronut you probably haven't heard of them tousled.",
            "Raclette portland tofu ugh, synth selfies labore vexillologist chambray. Esse chartreuse chia, squid hammock cold-pressed cray. Poutine kinfolk do consequat vaporware exercitation. ",
            "Truffaut irure echo park, wayfarers activated charcoal portland dolore culpa hammock irony mollit gluten-free plaid cliche. Tumeric keffiyeh sapiente meh, disrupt jianbing hot chicken deserunt letterpress succulents eiusmod hell of pork belly anim eu. ",
            "Banh mi kinfolk cillum +1 chia, copper mug fixie nostrud commodo hot chicken actually. Deep v four dollar toast DIY banh mi, reprehenderit labore occupy try-hard. ",
            "Taxidermy unicorn velit laborum, brooklyn you probably haven't heard of them aesthetic poke. Proident la croix VHS cupidatat anim swag franzen, disrupt yr pok pok freegan gastropub chambray."
        ];
        $quantity = rand(20, 100);

        $out = [];
        for($i = 1; $i <= $quantity ; $i += 1){
            $img_name = '00'.rand(1, 8).'.jpg';
            shuffle($titles);
            shuffle($text);
            array_push($out, [
                'id'    => $i,
                'img'   => 'http://localhost/massive-web/src/img/music-pack/'.$img_name,
                'title' => $titles[0],
                'text'  => $text[0]
            ]);
        }
        return $out;
    }


}
