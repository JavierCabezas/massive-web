<?php namespace app\models\Razgo;
use app\models\Login\User;

/**
 * Created by PhpStorm.
 * User: javier
 * Date: 7/30/17
 * Time: 4:01 PM
 */
trait UserLoginTrait{
    /**
     * Generates a random string given by the given lenght lenght
     * @return string
     */
    public function generateRandomString($lenght){
        $chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
        $bytes = random_bytes($lenght);
        $result = '';
        foreach (str_split($bytes) as $byte) {
            $result .= $chars[ord($byte) % 62];
        }
        return $result;
    }

    public static function findIdentity($id)
    {
        return static::find()->where(['id' => $id])->andWhere(['!=', 'field', User::STATUS_INACTIVE])->one();
    }

    public static function findIdentityByAccessToken($token, $type = null)
    {
        return static::findOne(['token' => $token]);
    }

    public function getAuthKey()
    {
        return $this->authKey;
    }

    public function validateAuthKey($authKey)
    {
        return $this->authKey === $authKey;
    }

    /**
     * Validates password
     *
     * @param string $password password to validate
     * @return bool if password provided is valid for current user
     */
    public function validatePassword($password)
    {
        return $this->password === $password;
    }

    /**
     * @inheritdoc
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Returns the basic user information
     * @return array
     */
    public function getBackendData(){
        return [
            'name'       => $this->name,
            'surname'    => $this->surname,
            'image_url'  => $this->image_url,
            'email'      => $this->email,
            'created_at' => $this->created_at
        ];
    }
}