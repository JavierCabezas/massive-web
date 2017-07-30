<?php

use yii\db\Migration;

/**
 * Handles the creation of table `user`.
 */
class m170730_160358_create_user_table extends Migration
{
    /**
     * @inheritdoc
     */
    public function up()
    {
        $this->createTable('user', [
            'id' => $this->primaryKey(),
            'name' => $this->string('200'),
            'surname' => $this->string('200'),
            'status' => $this->smallInteger()->notNull()->defaultValue(10),
            'image_url' => $this->string(),
            'email' => $this->string()->notNull()->unique(),
            'google_token' => $this->string(),
            'google_id' => $this->string(),
            'facebook_token' => $this->string(),
            'facebook_id' => $this->string(),
            'token' => $this->string(), //This is OUR token
            'auth_key' => $this->string(32)->notNull(),
            'password_hash' => $this->string()->notNull(),
            'password_reset_token' => $this->string()->unique(),
            'created_at' => $this->integer()->notNull(),
            'updated_at' => $this->integer()->notNull(),
        ]);
    }

    /**
     * @inheritdoc
     */
    public function down()
    {
        $this->dropTable('user');
    }
}
