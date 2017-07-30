<template>
    <div class="top-bar">
        <div class="container">
            <div class="row">
                <div class="col-sm-12 text-right">
                    <ul class="list-inline">
                        <li v-if="!login_status.state.isLoggedIn">
                            <a href="#/user/login"><i class="fa fa-user"></i>{{ t('login') }} </a>
                        </li>
                        <li v-if="login_status.state.isLoggedIn">
                            <a href="#/user/profile"><i class="fa fa-user"></i>{{ t('account') }} </a>
                        </li>
                        <li class="lang-dropdown">
                            <a> {{ t('active_lang') }}  </a>
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
    export default {
        locales: {
            es_ES: {
                account: 'Mi cuenta',
                login: 'Ingresar',
                active_lang: 'Español'
            },
            en_US: {
                account: 'My account',
                login: 'Login',
                active_lang: 'English'
            }
        },
        data () {
            return {
                login_status: login_status
            }
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