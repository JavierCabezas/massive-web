<template>
    <div class="row">
        <g-signin-button v-if="!login_status.state.isLoggedIn"
                         :params="googleSignInParams"
                         @success="onSignInSuccess"
                         @error="onSignInError">
            Sign in with Google
        </g-signin-button>

        <a href="#" v-if="login_status.state.isLoggedIn" @click.prevent="signOut" class="btn btn-primary">Log out</a>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                googleSignInParams: {
                    client_id: '629002016280-i54mtm5av310m0as2i279s7aq5cvl37l.apps.googleusercontent.com'
                },
                login_status: login_status
            }
        },
        methods: {
            onSignInSuccess (googleUser) {
                let vm = this;
                const profile = googleUser.getBasicProfile();
                let user_data = {
                    token: googleUser.getAuthResponse().id_token,
                    id: profile.getId(),
                    name: profile.getName(),
                    image_url: profile.getImageUrl(),
                    email: profile.getEmail()
                };
                $.ajax({
                    url: vm.url_backend + '/api/user/login',
                    method: 'POST',
                    data:{
                        type: 'google',
                        user_data: user_data
                    },
                    success: function (result) {
                        vm.login_status.state =  vm.login_status.updateLogin('asdfasdf');
                    }
                });
            },
            onSignInError (error) {
                console.log('OH NOES', error)
            },
            signOut() {
                let auth2 = gapi.auth2.getAuthInstance();
                let vm = this;
                auth2.signOut().then(function () {
                    vm.login_status.state =  vm.login_status.logOut();
                    console.log('User signed out.');
                });
            },
        }
    }
</script>

<style>
    .g-signin-button {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 3px;
        background-color: #3c82f7;
        color: #fff;
        box-shadow: 0 3px 0 #0f69ff;
    }
</style>