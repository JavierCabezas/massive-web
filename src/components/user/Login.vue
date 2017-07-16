<template>
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <div class="sky-form-login">
                    <h1 class="text-center"><i class="fa fa-unlock"></i> &nbsp; {{ t('login') }} </h1>

                    <h4> {{ t('login_details') }} </h4>


                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
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
        methods:{

        }
    }
</script>