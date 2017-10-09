import { routes } from './routes'
import Vue from 'vue'
import VueRouter from 'vue-router'
import VueTranslate from 'vue-translate-plugin';
import App from './App.vue'
import GSignInButton from 'vue-google-signin-button'
import FBSignInButton from 'vue-facebook-signin-button'
import Vuex, { Store } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import VueSweetAlert from 'vue-sweetalert'


Vue.use(Vuex);
Vue.use(GSignInButton);
Vue.use(VueRouter);
Vue.use(VueTranslate);
Vue.use(FBSignInButton);
Vue.use(VueSweetAlert);


const router = new VueRouter({
    routes
});

export const store = new Store({
  state: {
      is_logged_in: false,
      token: null,
      number_of_items_on_cart: 0,
      music_pack_on_cart: {},
      music_tracks_on_cart: {}
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
      },
      add_music_pack_to_cart(state, music_pack, quantity = 1){
          if(state.music_pack_on_cart[music_pack.id] === undefined){
              state.music_pack_on_cart[music_pack.id] = music_pack;
              state.music_pack_on_cart[music_pack.id]['quantity'] = 0;
          }
          state.music_pack_on_cart[music_pack.id]['quantity'] += quantity;
      },
      add_music_track_to_cart(music_track, quantity = 1){

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
