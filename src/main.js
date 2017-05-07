import Vue from 'vue'
import VueRouter from 'vue-router'
import VueTranslate from 'vue-translate-plugin';
import { routes } from './routes'
import App from './App.vue'

Vue.use(VueRouter);
Vue.use(VueTranslate);

const router = new VueRouter({
    routes
});

new Vue({
    el: '#app',
    router,
    render: h => h(App)
});
