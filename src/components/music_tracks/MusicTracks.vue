<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1>Music Tracks</h1>
            </div>
        </div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>
        <div class="space-60"></div>
        <div class="row">
            <div class="col-md-12">
                <music-track-list :items="items"></music-track-list>
            </div>
        </div>
    </div>
</template>

<script>
    import MusicTrackList from './MusicTrackList.vue'
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default {
        data () {
            return {
                items: [ ],
                crumbs: {
                    nav: [
                        {
                            link: 'home',
                            name_en: 'Home',
                            name_es: 'Inicio'
                        }
                    ],
                    current: {
                        es: 'Canciones sueltas',
                        en: 'Music tracks'
                    }
                }
            }
        },
        created: function () {
            let vm = this;
            let url = vm.url_backend + 'music_track/index';

            $.ajax({
                url: url,
                success: function (result) {
                    vm.items = result;
                }
            });
        },
        components: {
            musicTrackList: MusicTrackList,
            breadCrumbs: BreadCrumbs
        }
    }
</script>