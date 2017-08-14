<template>
    <div class="row">
        <p>User data:</p>
        <ul>
            <li> Name: {{user_data.name}} {{user_data.surname}}</li>
            <li> Picture: <img :src="user_data.image_url" :alt="user_data.name"> </li>
            <li> Email: {{user_data.email}}</li>
        </ul>

        <a href="#" @click.prevent="logout()" class="btn btn-primary btn-lg">
            <span class="glyphicon glyphicon-log-out"> </span> {{ t('logout') }}
        </a>
    </div>
</template>

<script>
    import { store } from '../../main'

    export default {
        data () {
            return {
                user_data: { name: "",  surname: "",  image_url: "",  email: "" },
            }
        },
        locales: {
            es_ES: { logout: 'Cerrar sesión' },
            en_US: { logout: 'Logout' }
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
            var vm = this;
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
//                    router.go('/user/login');
                }
            },
            logout() {
                store.commit('delete_token_and_logout')
                this.check_if_logged_in()
            }
        }
    }
</script>