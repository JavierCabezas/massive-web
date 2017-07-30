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
     * Generates a random 256 lenght token to assign to a new user
     * @return string
     */
    public function generateToken(){
        $chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
        $bytes = random_bytes(256);
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
}