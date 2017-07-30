<?php namespace app\models\Razgo;
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 7/30/17
 * Time: 4:11 PM
 */
use app\models\Login\User;
use Google_Client;

trait UserGoogleLoginTrait{
    /**
     * Verifies the identity of a google login.
     * @param $client_id
     * @param $id_token
     * @return bool
     */
    public static function verify($id_token){
        $client = new Google_Client(['client_id' => User::GOOGLE_USER_ID]);
        $payload = $client->verifyIdToken($id_token);
        if ($payload) {
            return true;
        } else {
            return false;
        }
    }

}