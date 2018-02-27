<template>
    <div id="emojis">
        <fieldset>
            <input type="text" v-model="search" placeholder="search for emoji">

            <select v-model="main_category_query">
                <option value="" disabled hidden>Category</option>
                <option v-for="category_obj in categories" v-bind:value="category_obj.name">
                    {{ category_obj.name }}
                </option>
            </select>

            <select v-model="sub_category_query">
                <option value="" disabled hidden>Sub Category</option>
                <option v-for="subcategory in selected_subcategories">
                    {{ subcategory }}
                </option>
            </select>
        </fieldset>
            

        <div class="all-emojis" v-for="emoji in emojis">
            <span>{{ emoji.shortcode }}</span>
        </div>


        <!-- <div v-for="emoji, alias in filtered_emojis">
            <span>{{ emoji }} - {{ alias }}</span>
        </div> -->
        
    </div>
</template>


<script>
    import _ from 'lodash';

    export default {
        props: {
        },

        data() {
            return {
                emojis: [],
                categories: {},
                search: '',
                main_category_query: '',
                sub_category_query: '',
                fresh_search: false,
                bottom: false,
                // baseUrl: 'http://localhost:8000/',
                resourceUrl: 'http://localhost:8000/emojis?flat=true',
                categoryUrl: 'http://localhost:8000/categories'
            }
        },

        methods: {
            copy: function(emoji) {
              this.$clipboard(emoji);
            },

            bottomVisible() {
                const scrollY = window.scrollY;
                const visible = document.documentElement.clientHeight;
                const pageHeight = document.documentElement.scrollHeight;
                const bottomOfPage = visible + scrollY >= pageHeight;
                return bottomOfPage || pageHeight < visible;
            },

            loadCategories() {
                this.$http.get(this.categoryUrl)
                .then(function(data) {
                    console.log('category data', data);
                    return data.json()
                })
                .then(function(data) {
                    this.categories = data.results;
                })
                .catch(function(error) {
                    console.log('Error! Could not reach the API. ' + error);
                })
            },

            loadEmoji() {
                if (this.resourceUrl != null) {

                    this.$http.get(this.resourceUrl)
                    .then(function(data) {
                        console.log(data);
                        return data.json()
                    })
                    .then(function(data) {
                        if (this.fresh_search) {
                            this.emojis = [];
                            this.emojis.push(...data.results);
                        }
                        else {
                            this.emojis.push(...data.results);
                        }
                        this.resourceUrl = data.next;
                    })
                    .catch(function(error) {
                        console.log('Error! Could not reach the API. ' + error);
                    })
                } 
            },

            debounceSearch: _.debounce(function() {
                // let query_param = this.search;
                // let sub_cat_param = this.main_category_query;
                // let main_cat_param = this.sub_category_query;

                let url = `http://localhost:8000/emojis?q=${this.search}&main_category=${this.main_category_query}&sub_category=${this.sub_category_query}`;
                this.resourceUrl = url;
                this.fresh_search = true;
                this.loadEmoji();

            }, 2000)

        },

        computed: {
            filtered_emojis: function() {
                
                // Build array of keys that match the search term
                let search_keys = Object.keys(this.emojis).filter(
                    (alias) => alias.match(this.search)
                );

                // Build new object from search_keys array
                let copy = {};

                search_keys.map(key => {
                    copy[key] = this.emojis[key];
                });

                return copy;
            },

            selected_subcategories: function() {
                if (this.main_category_query) {
                    let selected_category = this.categories.find(obj => 
                        (obj.name == this.main_category_query)
                    )
                    // returning list
                    // console.log(selected_category);
                    this.sub_category_query = selected_category.subcategories[0];
                    return selected_category.subcategories
                }
            }
        },

        watch: {
            bottom() {
                if (this.bottom) {
                    // console.log('BOTTOM: ', this.bottom);
                    // console.log('BOTTOM VISIBLE: ', this.bottomVisible());
                    this.fresh_search = false;
                    this.loadEmoji();
                }
            },

            // search() {
            //     this.debounceSearch();
            // }
        },

        created() {
            window.addEventListener('scroll', () => {
                this.bottom = this.bottomVisible();
            })
            this.fresh_search = true;
            this.loadEmoji();
            this.loadCategories();

            let vm = this;

            this.$watch(vm => [
                vm.search, 
                vm.main_category_query, 
                vm.sub_category_query
            ].join(), val => {
                vm.debounceSearch();
            })
        }
    }
</script>


<style scoped>

    input {
        width: 100%;
        height: 50px;
        margin: 20px 0;
        display: inline-block;
        text-align: center;
    }

    #emojis {
        width: 100%;
        max-width: 1200px;
        margin: 40px auto;
        padding: 0 20px;
        box-sizing: border-box;
        text-align: center;
    }

</style>