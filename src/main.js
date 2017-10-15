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


export const router = new VueRouter({
    routes
});

export const store = new Store({
  state: {
      is_logged_in: false,
      token: null,
      number_of_items_on_cart: 0,
      music_packs_on_cart: {},
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
      add_music_pack_to_cart(state, payload){
          state.music_packs_on_cart[payload.music_pack.id] = payload.music_pack;
          state.number_of_items_on_cart += 1;
      },
      add_music_track_to_cart(state, payload){
          state.music_tracks_on_cart[payload.music_track.id] = payload.music_track;
          state.number_of_items_on_cart += 1;
      },
      remove_music_pack_from_cart(state, payload){
          delete state.music_packs_on_cart[payload.music_pack_id];
          state.number_of_items_on_cart -= 1;
      },
      remove_music_track_from_cart(state, payload){
          delete state.music_tracks_on_cart[payload.music_track_id] ;
          state.number_of_items_on_cart -= 1;
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

Vue.filter('cash', function(value) {
   const pieces = parseFloat(value).toFixed(2).split('');
    let ii = pieces.length - 3;
    while ((ii-=3) > 0) {
        pieces.splice(ii, 0, ',')
    }
    return "$" + pieces.join('')
});


new Vue({
    el: '#app',
    router,
    render: h => h(App)
});
