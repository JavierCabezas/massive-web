<template>
    <div>
        <ul class="breadcrumb">
            <li v-for="item in breadcrumbs">
                <a :href="item.link">{{item.name}}</a>
            </li>
            <li v-for="item in currentBreadcrumb" class="current">
               {{item.name}}
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                breadcrumbs: [
                    {
                        link: '#',
                        name: 'Link 1',
                    },
                    {
                        link: '#',
                        name: 'Link 2',
                    },
                    {
                        link: '#',
                        name: 'Link 3',
                    }
                ],
                currentBreadcrumb: [
                    {
                        link: 'src/img/portfolio/pms.jpg',
                        name: 'Link actual'
                    }
                ]
            }
        },
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