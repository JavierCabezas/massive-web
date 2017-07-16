<template>
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <div class="sky-form-login">
                    <h1 class="text-center"><i class="fa fa-unlock"></i> &nbsp; {{ t('login') }} </h1>

                    <h4> {{ t('login_details') }} </h4>

                    <g-signin-button
                            :params="googleSignInParams"
                            @success="onSignInSuccess"
                            @error="onSignInError">
                        Sign in with Google
                    </g-signin-button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                /**
                 * The Auth2 parameters, as seen on
                 * https://developers.google.com/identity/sign-in/web/reference#gapiauth2initparams.
                 * As the very least, a valid client_id must present.
                 * @type {Object}
                 */
                googleSignInParams: {
                    client_id: '629002016280-i54mtm5av310m0as2i279s7aq5cvl37l.apps.googleusercontent.com'
                }
            }
        },
        locales: {
            es_ES: {
                login: 'Ingreso a tu cuenta',
                login_details: 'Los métodos de ingreso disponibles son por medio de una cuenta Google o Facebook.'
            },
            en_US: {
                login: 'Log in to your account',
                login_details: 'The avaiable login methods are via Google or Facebook accounts.'
            }
        },
        methods: {
            onSignInSuccess (googleUser) {
                // `googleUser` is the GoogleUser object that represents the just-signed-in user.
                // See https://developers.google.com/identity/sign-in/web/reference#users
                const profile = googleUser.getBasicProfile() // etc etc
                console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
                console.log('Name: ' + profile.getName());
                console.log('Image URL: ' + profile.getImageUrl());
                console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
            },
            onSignInError (error) {
                // `error` contains any error occurred.
                console.log('OH NOES', error)
            }
        }
    }
</script>

<style>
    .g-signin-button {
        /* This is where you control how the button looks. Be creative! */
        display: inline-block;
        padding: 4px 8px;
        border-radius: 3px;
        background-color: #3c82f7;
        color: #fff;
        box-shadow: 0 3px 0 #0f69ff;
    }
</style>