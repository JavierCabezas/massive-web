<template>
    <div class="top-bar">
        <div class="container">
            <div class="row">
                <div class="col-sm-12 text-right">
                    <ul class="list-inline">
                        <li v-if="!is_user_logged_in">
                            <router-link  tag="a" :to="{ name: 'login'}" > <i class="fa fa-user"></i>{{ t('login') }}</router-link>
                        </li>
                        <li v-if="is_user_logged_in">
                            <router-link  tag="a" :to="{ name: 'profile'}" > <i class="fa fa-user"></i>{{ t('account') }} </router-link>
                        </li>
                        <li v-if="is_user_logged_in">
                            <router-link  tag="a" :to="{ name: 'shopping-cart'}" > <i class="fa fa-shopping-cart"></i>{{ t('shopping_cart') }} </router-link>
                            <span class="num" v-if="store.state.number_of_items_on_cart > 0">
                                {{store.state.number_of_items_on_cart}}
                            </span>
                        </li>
                        <li class="lang-dropdown">
                            <a>
                                <img v-if="$translate.current == 'en_US'" src="../../img/flag_en.png">
                                <img v-if="$translate.current == 'es_ES'" src="../../img/flag_es.png">
                                {{ t('active_lang') }}
                            </a>
                            <div class="lang-drop-menu">
                                <a @click.prevent="changeLang('en_US')"><img src="../../img/flag_en.png"> English </a>
                                <a @click.prevent="changeLang('es_ES')"><img src="../../img/flag_es.png"> Spanish </a>
                            </div>
                        </li>
                        <li><a href="#" @click.prevent="openSearch()" class="search-toggle"><i class="fa fa-search"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { store } from '../../main'

    export default {
         data () {
            return {
                store: store
            }
        },
        locales: {
            es_ES: {
                account: 'Mi cuenta',
                login: 'Ingresar',
                active_lang: 'Español',
                shopping_cart: 'Carrito de compras'
            },
            en_US: {
                account: 'My account',
                login: 'Login',
                active_lang: 'English',
                shopping_cart: 'Shopping cart'
            }
        },
        computed: {
            is_user_logged_in() {
                return store.state.is_logged_in;
            },
        },
        methods:{
            changeLang(lang){
                this.$translate.setLang(lang);
            },
            openSearch() {
                $(".search-toggle").click(function(){
                    $(".search-bar").slideDown('fast');
                });
            }
        }
    }
</script>