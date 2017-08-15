<template>
    <fb-signin-button
            :params="fbSignInParams"
            @success="onSignInSuccess"
            @error="onSignInError">
        Sign in with Facebook
    </fb-signin-button>
</template>

<script>
    export default {
        data () {
            return {
                fbSignInParams: {
                    scope: 'email,user_likes',
                    return_scopes: true
                }
            }
        },
        methods: {
            onSignInSuccess (response) {
                FB.api('/me', dude => {
                    console.log(`Good to see you, ${dude.name}.`)
                })
            },
            onSignInError (error) {
                console.log('OH NOES', error)
            }
        }
    }
</script>

<style>
    .fb-signin-button {
        display: inline-block;
        border-radius: 3px;
        background-color: #4267b2;
        color: #fff;
        width: 40%;
        margin-left: 30%;
        margin-right: auto;
        margin-bottom: 1%;
        font-size: 2.5em;
        padding: 2% 0;
        text-align: center;
    }
</style>