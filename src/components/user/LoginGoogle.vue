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
        methods: {
            onSignInSuccess (googleUser) {
                let vm = this;
                const profile = googleUser.getBasicProfile(); // etc etc
                vm.isLoggedIn = true;
                console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
                console.log('Name: ' + profile.getName());
                console.log('Image URL: ' + profile.getImageUrl());
                console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
            },
            onSignInError (error) {
                console.log('OH NOES', error)
            },
            signOut() {
                let auth2 = gapi.auth2.getAuthInstance();
                let vm = this;
                auth2.signOut().then(function () {
                    console.log('User signed out.');
                });
                vm.isLoggedIn = false;
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