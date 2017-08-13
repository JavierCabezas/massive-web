import { routes } from './routes'
import Vue from 'vue'
import VueRouter from 'vue-router'
import VueTranslate from 'vue-translate-plugin';
import App from './App.vue'
import GSignInButton from 'vue-google-signin-button'
import FBSignInButton from 'vue-facebook-signin-button'
import Vuex, { Store } from 'vuex';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);
Vue.use(GSignInButton);
Vue.use(VueRouter);
Vue.use(VueTranslate);
Vue.use(FBSignInButton);

const router = new VueRouter({
    routes
});

export const store = new Store({
  state: {
      is_logged_in: false,
      token: null
  },
  plugins: [createPersistedState()],
  mutations: {
      login_with_token(state, token) {
            state.is_logged_in = true;
            state.token = token;
      },
      delete_token_and_logout(state){
          state.is_logged_in = false;
          state.token = null;
      }
  }
});

Vue.mixin({
    data: function() {
        return {
            get url_backend() {
                return "http://127.0.0.1:8000/";
            }
        }
    }
});

new Vue({
    el: '#app',
    router,
    render: h => h(App)
});
