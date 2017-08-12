<template>
    <div class="row">
        <g-signin-button v-if="!isLoggedIn"
                         :params="googleSignInParams"
                         @success="onSignInSuccess"
                         @error="onSignInError">
            Sign in with Google
        </g-signin-button>


        <a href="#" v-if="isLoggedIn" @click.prevent="signOut" class="btn btn-primary">Log out</a>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                googleSignInParams: {
                    client_id: '629002016280-i54mtm5av310m0as2i279s7aq5cvl37l.apps.googleusercontent.com'
                },
                isLoggedIn: false
            }
        },
        created: function() {
            //this.isLoggedIn = this.is_logged_in
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
                        localStorage.setItem("token", result);
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