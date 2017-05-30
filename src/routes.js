/**
 * Created by javier on 5/7/17.
 */
import About from './components/sections/About.vue'
import Home from './components/main/Home.vue'
import Faq from './components/sections/Faq.vue'
import Blog from './components/sections/Blog.vue'
import BlogPost from './components/sections/BlogPost.vue'
import MusicPacks from './components/music_packs/MusicPacks.vue'
import MusicPackDetail from './components/music_packs/MusicPackDetail.vue'

export const routes = [
    { path: '', component: Home },
    { path: '/home', component: Home },
    { path: '/about', component: About },
    { path: '/faq', component: Faq },
    { path: '/blog', component: Blog },
    { path: '/blog/:id', component: BlogPost },
    { path: '/music-pack', component: MusicPacks },
    { path: '/music-pack/:id', component: MusicPackDetail, name: 'musicPackDetail' }
];