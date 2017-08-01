<template>
    <div class="row">
        <p>User data:</p>
        <ul>
            <li> Name: {{user_data.name}} {{user_data.surname}}</li>
            <li> Picture: <img :src="user_data.image_url" :alt="user_data.name"> </li>
            <li> Email: {{user_data.email}}</li>
        </ul>
    </div>
</template>

<script>

    export default {
        data () {
            return {
                is_logged_in: login_status.state.isLoggedIn,
                user_data: login_status.user_data
            }
        },
        created() {
            this.check_if_logged_in();
        },
        methods: {
            check_if_logged_in(){
                if(!this.is_logged_in){
//                    router.go('/user/login');
                }
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