<?php namespace app\models\Razgo;
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 7/30/17
 * Time: 4:11 PM
 */
use app\models\Login\User;
use Google_Client;
use Yii;

trait UserGoogleLoginTrait{
    /**
     * Verifies the identity of a google login.
     * @param $client_id
     * @param $id_token
     * @return bool
     */
    public static function verify($id_token){
        $client = new Google_Client(['client_id' => User::GOOGLE_USER_ID]);
        /**
         * $payload = [
         *      "azp":"GOOGLE_USER_ID", (Unused, for android app)
         *      "aud":"GOOGLE_USER_ID", (Used)
         *      "sub": Unused (and not sure what it does)
         *      "email": User email,
         *      "email_verified":bool,
         *      "at_hash": string
         *      "iss": Always accounts.google.com
         *      "iat": timestamp
         *      "exp": timestamp
         *      "name": name family name
         *      "picture": URL,
         *      "given_name": Name,
         *      "family_name": Family name,
         *      "locale": en
         * ]
         */
        $payload = $client->verifyIdToken($id_token);
        if ($payload) {
            if($payload['aud'] == User::GOOGLE_USER_ID && $payload['iss'] == "accounts.google.com"){
                return $payload;
            }
        }
        return false;
    }

    /**
     * Creates a new user given the data on the $payload variable.
     * @see UserGoogleLoginTrait::verify() for payload format
     * @param $payload
     * @param $user_data with the format [
     *      token: Google token (string)
     *      id: int
     *      name: given name + family name
     *      image_url: URL,
     *      email: email
     * ]
     * @return bool | User instance of the newly created user
     */
    public static function createGoogleUser($payload, $user_data){
        $u = new User();
        $u->email = $payload['email'];
        if( isset($payload['given_name']) && isset($payload['family_name']) && $payload['given_name'] != "" && $payload['family_name'] != ""){
            $u->name = $payload['given_name'];
            $u->surname = $payload['family_name'];
        }else{
            $u->name = $payload['name'];
        }
        $u->image_url = $payload['picture'];
        $u->google_id = $user_data['id'];
        $u->google_token = $user_data['token'];

        if(!$u->save(false)){
            Yii::error('These are the errors given by getErrors:' . print_r($u->getErrors()));
            return false;
        }
        return $u;
    }

}