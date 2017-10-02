<template>
    <div>
        <ul class="breadcrumb">
            <li v-for="item in crumbs.nav">
                <router-link to="item.link" v-if="$translate.current == 'en_US'">
                    {{item.name_en }}
                </router-link>
                <router-link :to="item.link" v-if="$translate.current == 'es_ES'">
                    {{item.name_es}}
                </router-link>
            </li>
            <li class="current">
                <span v-if="$translate.current == 'en_US'"> {{crumbs.current.en}} </span>
                <span v-if="$translate.current == 'es_ES'"> {{crumbs.current.es}} </span>
            </li>
        </ul>

    </div>
</template>

<script>
    export default {
        /*
            Crumbs must be in the format:
            'nav' : Array of object in the format [
                {
                    link: string,
                    name_es: string,
                    name_en: string
                },
                {
                    ...
                },
                ...
            ],
            'current: {
                'es': string
                'en': string
                }
            }
         */
        props: [ 'crumbs' ]
    }
</script>

<style>
    ul.breadcrumb {
        list-style-type: none;
        clear: both;
        height: auto;
        overflow: auto;
    }
    ul.breadcrumb li {
        float: left;
        padding: 0;
        width: auto;
        color: #B67E90;
    }
    ul.breadcrumb li.current {
        color: #6E5C7A;
        font-weight: bold;
    }

    ul.breadcrumb li.current::after {
        content: none;
    }
</style>