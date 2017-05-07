/**
 * Created by javier on 5/7/17.
 */
import About from './components/sections/About.vue'
import Home from './components/main/Home.vue'
import Faq from './components/sections/Faq.vue'
import Blog from './components/sections/Blog.vue'

export const routes = [
    { path: '', component: Home },
    { path: '/home', component: Home },
    { path: '/about', component: About },
    { path: '/faq', component: Faq },
    { path: '/blog', component: Blog }
];