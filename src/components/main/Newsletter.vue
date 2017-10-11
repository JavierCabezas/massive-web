<template>
    <div class="newsletter container">
        <div class="row">
            <div class="col-md-5">
                <h3> {{t('subscribe')}} </h3>
                <p> {{t('and')}} </p>
            </div>
            <div class="col-md-7">
                <form role="form" method="post" action="#" class="subscribe-form assan-newsletter">
                    <div class="row">
                        <div class="col-sm-8">
                            <div class="form-group">
                                <input v-model='email_field' type='text' class='form-control' name='email' placeholder='Email'>
                            </div>
                        </div>
                        <div class="col-sm-4 text-center">
                            <div>
                                <button @click.prevent="subscribe()" class="newsletter-btn" name="submit" type="submit"> {{t('sub_button')}}</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
     export default {
         props: ['blog_posts'],
         locales: {
            en_US: {
                subscribe: 'Subscribe to our Newsletter',
                sub_button: 'Subscribe',
                and: 'And get all the news about MassiveWave'
            },
            es_ES: {
                subscribe: 'Suscríbete a nuestro newsletter',
                sub_button: 'Suscribirse',
                and: 'Y entérate de todas las novedades de MassiveWave'
            }
         },
         data () {
            return {
                email_field: ""
            }
         },
         methods:{
            subscribe(){
                let vm = this;
                let url = vm.url_backend + 'newsletter/add';
                let swal_texts = { 'title':'', 'text': '' };

                $.ajax({
                    url: url ,
                    type: 'POST',
                    data: {
                        email: vm.email_field
                    },
                    success: function (result) {
                       if(vm.$translate.current === 'en_US'){
                           swal_texts.title = 'Success!';
                           swal_texts.text = 'Your email address was successfully added to our database.';
                       }
                       else{
                           swal_texts.title = 'Éxito!';
                           swal_texts.text = 'Registramos tu dirección de correo electrónico con éxito';
                       }
                       vm.$swal( swal_texts.title, swal_texts.text, 'success');
                       vm.email_field = '';
                    },
                    error: function(xhr) {
                        if(xhr.status === 400){
                            if(vm.$translate.current === 'en_US'){
                                swal_texts.title = 'Email problem';
                                swal_texts.text = 'It seems that the email address given is not a valid e-mail address.';
                            }
                            else{
                                swal_texts.title = 'Problema de email';
                                swal_texts.text = 'Aparentemente la dirección de correo electrónico ingresada no es válida.';
                            }
                            vm.$swal( swal_texts.title, swal_texts.text, 'error');
                        }
                        if(xhr.status === 409){
                            if(vm.$translate.current === 'en_US'){
                                swal_texts.title = 'We already know each other!';
                                swal_texts.text = 'The email address given is already on our database.';
                            }
                            else{
                                swal_texts.title = 'Ya nos conocemos!';
                                swal_texts.text = 'La dirección de correo electrónico ingresada ya está en nuestra base de datos.';
                            }
                            vm.$swal( swal_texts.title, swal_texts.text, 'info');
                        }
                        console.log(xhr.status);
                    }
                });
            }
         }
     }
 </script>