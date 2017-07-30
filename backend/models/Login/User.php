<?php namespace app\models\Login;
/**
 * Created by PhpStorm.
 * User: javier
 * Date: 7/30/17
 * Time: 3:46 PM
 */
use Yii;
use app\models\Razgo\{UserLoginTrait, UserGoogleLoginTrait};

/**
 * This is the model class for table "user".
 *
 * @property int $id
 * @property string $name
 * @property string $surname
 * @property int $status
 * @property string $image_url
 * @property string $email
 * @property string $google_token
 * @property string $google_id
 * @property string $facebook_token
 * @property string $facebook_id
 * @property string $token
 * @property string $auth_key
 * @property string $password_hash
 * @property string $password_reset_token
 * @property int $created_at
 * @property int $updated_at
 */
class User extends \yii\base\Object implements \yii\web\IdentityInterface
{
    use UserLoginTrait;
    use UserGoogleLoginTrait;

    const STATUS_USER_ACTIVE = 10;
    const STATUS_ADMIN_ACTIVE = 11;
    const STATUS_INACTIVE = 12;

    const GOOGLE_USER_ID = '629002016280-i54mtm5av310m0as2i279s7aq5cvl37l.apps.googleusercontent.com';

    public static function tableName()
    {
        return 'user';
    }

    public function rules()
    {
        return [
            [['status', 'created_at', 'updated_at'], 'integer'],
            [['email', 'auth_key', 'password_hash', 'created_at', 'updated_at'], 'required'],
            [['name', 'surname'], 'string', 'max' => 200],
            [['image_url', 'email', 'google_token', 'google_id', 'facebook_token', 'facebook_id', 'token', 'password_hash', 'password_reset_token'], 'string', 'max' => 255],
            [['auth_key'], 'string', 'max' => 32],
            [['email'], 'unique'],
            [['password_reset_token'], 'unique'],
        ];
    }

    public function attributeLabels()
    {
        return [
            'id' => 'ID',
            'name' => 'Name',
            'surname' => 'Surname',
            'status' => 'Status',
            'image_url' => 'Image URL',
            'email' => 'Email',
            'google_token' => 'Google Token',
            'google_id' => 'Google ID',
            'facebook_token' => 'Facebook Token',
            'facebook_id' => 'Facebook ID',
            'token' => 'Token',
            'auth_key' => 'Auth Key',
            'password_hash' => 'Password Hash',
            'password_reset_token' => 'Password Reset Token',
            'created_at' => 'Created At',
            'updated_at' => 'Updated At',
        ];
    }

}