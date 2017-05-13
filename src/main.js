import { routes } from './routes'
import Vue from 'vue'
import VueRouter from 'vue-router'
import VueTranslate from 'vue-translate-plugin';
import App from './App.vue'

Vue.use(VueRouter);
Vue.use(VueTranslate);

const router = new VueRouter({
    routes
});

Vue.mixin({
    data: function() {
        return {
            get url_backend() {
                return "http://localhost/massive-web/backend/web/index.php";
            }
        }
    }
});

new Vue({
    el: '#app',
    router,
    render: h => h(App)
});
