<template>
    <div class="col-md-3 col-md-offset-1">
        <div class="sidebar-widget">
            <h3> {{ t('filter') }}</h3>
            <ul class="list-unstyled">
                <li>
                    <a href="#" @click.prevent="change_category()">
                        <span v-if="selected_category_index !== -1"> {{ t('all_categories') }} </span>
                        <b v-if="selected_category_index === -1"> {{ t('all_categories') }} </b>
                    </a>
                </li>
                <li v-for="(c, idx) in categories">
                    <a v-if="$translate.current == 'en_US'" href="#" @click.prevent="change_category(idx)">
                        <span v-if="selected_category_index !== idx"> {{c.name_en}} </span>
                        <b v-if="selected_category_index === idx"> {{c.name_en}} </b>
                    </a>
                    <a v-if="$translate.current == 'es_ES'" href="#" @click.prevent="change_category(idx)">
                        <span v-if="selected_category_index !== idx"> {{c.name_es}} </span>
                        <b v-if="selected_category_index === idx"> {{c.name_es}} </b>
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    locales: {
            es_ES: {
                all_categories: 'Todas',
                filter: 'Filtro por categoría'
            },
            en_US: {
                all_categories: 'All',
                filter: 'Filter by category'
            }
        },
        props: [ 'categories', 'selected_category_index'],
        methods: {
            change_category: function(idx){
                this.$emit('category_changed', idx)
            }
        }
    }
</script>