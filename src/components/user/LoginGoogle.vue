<template>
    <div class="row">
        <g-signin-button v-if="!is_user_logged_in"
                         :params="googleSignInParams"
                         @success="onSignInSuccess"
                         @error="onSignInError">
            Sign in with Google
        </g-signin-button>


        <a href="#" v-if="is_user_logged_in" @click.prevent="logout()" class="btn btn-primary">Log out</a>
    </div>
</template>

<script>
    import { store } from '../../main'

    export default {
        data () {
            return {
                googleSignInParams: {
                    client_id: '629002016280-i54mtm5av310m0as2i279s7aq5cvl37l.apps.googleusercontent.com'
                },
            }
        },
        computed: {
            is_user_logged_in() {
                return store.state.is_logged_in;
            },
        },
        methods: {
            onSignInSuccess (googleUser) {
                let vm = this;
                const profile = googleUser.getBasicProfile();
                $.ajax({
                    url: vm.url_backend + 'user/login',
                    method: 'POST',
                    data:{
                        type: 'google',
                        user_token: googleUser.getAuthResponse().id_token,
                        user_id: profile.getId(),
                        user_name: profile.getName(),
                        user_image_url: profile.getImageUrl(),
                        user_email: profile.getEmail()
                    },
                    success: function (result) {
                        vm.login(result)
                    }
                });
            },
            onSignInError (error) {
                console.log('OH NOES', error)
            },
            signOut() {
                localStorage.setItem("token", "");
                let auth2 = gapi.auth2.getAuthInstance();
                let vm = this;
                auth2.signOut().then(function () {
                    console.log('User signed out.');
                    vm.logout()
                });
            },
            login(token) {
              store.commit('login_with_token', token)
            },
            logout() {
              store.commit('delete_token_and_logout')
            }
        }
    }
</script>

<style>
    .g-signin-button {
        display: inline-block;
        border-radius: 3px;
        background-color: #3c82f7;
        color: #fff;
        box-shadow: 0 3px 0 #0f69ff;
        width: 40%;
        margin-left: 30%;
        margin-right: auto;
        margin-bottom: 1%;
        font-size: 2.5em;
        padding: 2% 0;
        text-align: center;
    }
</style>