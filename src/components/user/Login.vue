<template>
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <div class="sky-form-login">
                    <h1 class="text-center"><i class="fa fa-unlock"></i> &nbsp; {{ t('login') }} </h1>

                    <h4> {{ t('login_details') }} </h4>

                    <login-google></login-google>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import LoginGoogle from './LoginGoogle.vue'

    export default {
        data () {
            return {
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
        components: {
            loginGoogle: LoginGoogle
        },
        methods: {

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