/**
 * Created by javier on 5/7/17.
 */
import Home from './components/main/Home.vue'

const About = resolve => {
    require.ensure(['./components/sections/About.vue'], () => {
        resolve(require('./components/sections/About.vue'));
    });
};

const Faq = resolve => {
    require.ensure(['./components/sections/Faq.vue'], () => {
        resolve(require('./components/sections/Faq.vue'));
    });
};

const Blog = resolve => {
    require.ensure(['./components/sections/Blog.vue'], () => {
        resolve(require('./components/sections/Blog.vue'));
    }, 'blog');
};

const BlogPost = resolve => {
    require.ensure(['./components/sections/BlogPost.vue'], () => {
        resolve(require('./components/sections/BlogPost.vue'));
    }, 'blog');
};

const MusicPacks = resolve => {
    require.ensure(['./components/music_packs/MusicPacks.vue'], () => {
        resolve(require('./components/music_packs/MusicPacks.vue'));
    }, 'music-pack');
};

const MusicPackSearch = resolve => {
    require.ensure(['./components/music_packs/MusicPackSearch.vue'], () => {
        resolve(require('./components/music_packs/MusicPackSearch.vue'));
    }, 'music-pack');
};

const MusicTracks = resolve => {
    require.ensure(['./components/music_tracks/MusicTracks.vue'], () => {
        resolve(require('./components/music_tracks/MusicTracks.vue'));
    }, 'music-track');
};

const MusicPackDetail = resolve => {
    require.ensure(['./components/music_packs/MusicPackDetail.vue'], () => {
        resolve(require('./components/music_packs/MusicPackDetail.vue'));
    }, 'music-pack');
};

const MusicTrackDetail = resolve => {
    require.ensure(['./components/music_tracks/MusicTrackDetail.vue'], () => {
        resolve(require('./components/music_tracks/MusicTrackDetail.vue'));
    }, 'music-track-detail');
};

const User = resolve => {
    require.ensure(['./components/user/Login.vue'], () => {
        resolve(require('./components/user/Login.vue'));
    }, 'login');
};

const Profile = resolve => {
    require.ensure(['./components/user/Profile.vue'], () => {
        resolve(require('./components/user/Profile.vue'));
    }, 'login');
};

const ShoppingCart = resolve => {
     require.ensure(['./components/user/ShoppingCart.vue'], () => {
        resolve(require('./components/user/ShoppingCart.vue'));
    }, 'shopping-cart');
};



export const routes = [
    { path: '', component: Home },
    { path: '/home', component: Home , name: 'home'},
    { path: '/about', component: About, name: 'about-us'},
    { path: '/faq', component: Faq, name: 'faq'},
    { path: '/blog', component: Blog, name: 'blog'},
    { path: '/blog/:id', component: BlogPost, name: 'blog-post'},
    { path: '/music-pack', component: MusicPacks, name:'music-packs' },
    { path: '/music-pack/search', component: MusicPackSearch, name: 'music-pack-search' },
    { path: '/music-track', component: MusicTracks, name: 'music-tracks' },
    { path: '/music-track/:id', component: MusicTrackDetail, name: 'music-track-detail' },
    { path: '/music-pack/:id', component: MusicPackDetail, name: 'music-pack-detail' },
    { path: '/user/login', component: User, name: 'login' },
    { path: '/user/profile', component: Profile, name: 'profile' },
    { path: '/user/shopping-cart', component: ShoppingCart, name: 'shopping-cart' }

];