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


export const routes = [
    { path: '', component: Home },
    { path: '/home', component: Home },
    { path: '/about', component: About },
    { path: '/faq', component: Faq },
    { path: '/blog', component: Blog },
    { path: '/blog/:id', component: BlogPost },
    { path: '/music-pack', component: MusicPacks },
    { path: '/music-track', component: MusicTracks },
    { path: '/music-pack/:id', component: MusicPackDetail, name: 'musicPackDetail' }
];