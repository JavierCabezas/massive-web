import { routes } from './routes'
import Vue from 'vue'
import VueRouter from 'vue-router'
import VueTranslate from 'vue-translate-plugin';
import App from './App.vue'
import GSignInButton from 'vue-google-signin-button'
import FBSignInButton from 'vue-facebook-signin-button'
import Vuex from 'vuex'

Vue.use(Vuex);
Vue.use(GSignInButton);
Vue.use(VueRouter);
Vue.use(VueTranslate);
Vue.use(FBSignInButton);

const router = new VueRouter({
    routes
});


Vue.mixin({
    data: function() {
        return {
            get url_backend() {
                return "http://127.0.0.1:8000/";
            },
            get is_logged_in() {
                return localStorage.getItem("token") !== null;
            }
        }
    }
});

new Vue({
    el: '#app',
    router,
    render: h => h(App)
});
