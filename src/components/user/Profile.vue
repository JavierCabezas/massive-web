<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>{{user_data.name}} {{user_data.surname}}</h1>
            </div>
        </div>
        <div class="row">
            <section class="profile col-sm-offset-1 col-sm-10">
                <div class="prof-image col-sm-12 col-md-1">
                    <img :src="user_data.image_url" :alt="user_data.name">
                </div>
                <div class="col-sm-12 col-md-11">
                    <p class="col-sm-9">
                        <b>{{user_data.name}} {{user_data.surname}}</b> |
                        <b>{{user_data.email}}</b>
                    </p>
                    <a href="#" @click.prevent="logout()" class="btn btn-primary btn-lg col-sm-3">
                        <span class="glyphicon glyphicon-log-out"> </span> {{ t('logout') }}
                    </a>
                </div>
            </section>

            <section class="music_profile col-sm-offset-1 col-sm-10">
                <h3>{{ t('musicpacks') }}</h3>
                <div class="container">
                    <div class="row">
                        <ul class="popularslider">
                            <li class="slide item_holder">
                                <h4 class="title"> Lalala </h4>
                            </li>
                            <li class="slide item_holder">
                                <h4 class="title"> Lalala </h4>
                            </li>
                            <li class="slide item_holder">
                                <h4 class="title"> Lalala </h4>
                            </li>
                            <li class="slide item_holder">
                                <h4 class="title"> Lalala </h4>
                            </li>
                            <li class="slide item_holder">
                                <h4 class="title"> Lalala </h4>
                            </li>
                        </ul>
                    </div>
                </div>

            </section>
            </section>
        </div>
    </div>
</template>

<script>
    import { store } from '../../main'
    import { router } from '../../main'

    export default {
        data () {
            return {
                user_data: { name: "",  surname: "",  image_url: "",  email: "" },
            }
        },
        locales: {
            es_ES: { logout: 'Cerrar sesión', musicpacks: 'Tus Paquetes de Música' },
            en_US: { logout: 'Logout', musicpacks: 'Your Music Packs' }
        },
        computed: {
            is_user_logged_in() {
                return store.state.is_logged_in;
            },
            user_token(){
                return store.state.token;
            }
        },
        created: function () {
            this.check_if_logged_in();
            let vm = this;
            $.ajax({
                url: vm.url_backend + 'user/get_user',
                data: { token: vm.user_token },
                method: 'POST',
                success: function (result) {
                    vm.user_data = result;
                }
            });
        },
        methods: {
            check_if_logged_in(){
                if(!this.is_user_logged_in){
                    if(!store.state.is_logged_in){
                        router.push({name: 'login'});
                    }
                }
            },
            logout() {
                store.commit('delete_token_and_logout');
                this.check_if_logged_in();
            }
        }
    }
</script>