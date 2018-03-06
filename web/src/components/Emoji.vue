<template>    
    <section>
        <div class="container top-space bottom-space">

            <div class="field is-mobile">
                <div class="control">
                    <input class="input is-medium is-rounded" v-model="search" type="text" placeholder="Search for Emoji">

                </div>
            </div>

            <div class="field is-grouped is-grouped-centered is-mobile">

                <div class="field">
                    <div class="control is-expanded">
                        <div class="select is-medium is-rounded">
                            <select v-model="main_category_query">
                                <option value="" selected disabled>Main Category</option>
                                <option value="">All</option>
                                <option v-for="category_obj in categories" v-bind:value="category_obj.name">
                                    {{ category_obj.name }}
                                </option>
                            </select>
                            
                        </div>
                    </div>
                </div>

                <div class="field">
                    <div class="control is-expanded">
                        <div class="select is-medium is-rounded">
                            <select v-model="sub_category_query">
                                <option value="" selected disabled>Sub Category</option>
                                <option value="">All</option>
                                <option v-for="subcategory in selected_subcategories">
                                    {{ subcategory }}
                                </option>
                            </select>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="container bottom-space">
            <div v-if="no_results_found">
                <div class="content has-text-centered">
                    <h4>No results for &ldquo;{{ search }}&rdquo; in selected categories</h4>
                    <div class="spinner ld ld-clock" style="animation-duration:2.5s">{{ emoji_no_results }}</div>
                </div>
            </div>
            <div v-else>
                <show-emoji v-bind:emojis="emojis"></show-emoji>
            </div>
        </div>

        <div class="container">
            <div v-show="loading">
                <div class="spinner ld ld-spin">{{ emoji_spinner }}</div>
            </div>
        </div>
        
    </section>
</template>


<script>
    import _ from 'lodash';
    import showEmoji from './showEmoji.vue';

    export default {
        components: {
            'show-emoji': showEmoji
        },

        data() {
            return {
                emoji_spinner: '\ud83e\udd14',
                emoji_no_results:'\ud83e\uddd0',
                loading: false,
                emojis: [],
                categories: {},
                search: '',
                main_category_query: '',
                sub_category_query: '',
                main_category_select_active: false,
                fresh_search: false,
                no_results_found: false,
                bottom: false,
                resourceUrl: 'http://localhost:8000/emoji?flat=true',
                categoryUrl: 'http://localhost:8000/categories'
            }
        },

        methods: {
            bottomVisible() {
                // https://scotch.io/tutorials/simple-asynchronous-infinite-scroll-with-vue-watchers

                const scrollY = window.scrollY;
                const visible = document.documentElement.clientHeight;
                const pageHeight = document.documentElement.scrollHeight;
                const bottomOfPage = visible + scrollY >= pageHeight;
                return bottomOfPage || pageHeight < visible;
            },

            loadCategories() {
                /* 
                    Get category data and store in this.categories.
                    ex. 
                    [
                        {
                            name: "Smileys & People",
                            subcategories: ["face-positive", ..., "clothing"]
                        },
                        ...
                    ]
                */
                this.$http.get(this.categoryUrl)
                .then(function(data) {
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
                /* 
                    Get emoji data, store in this.emojis, set resourceUrl to next page of paginated results.

                    ex.
                    [
                        {
                            "shortcode": "grinning_face",
                            "codepoint": "\\U0001F600",
                            "surrogate_pairs": "\"\\ud83d\\ude00\"",
                            "shortened_codepoint": "U+1F600" 
                        },
                        ...
                    ]
                */
                if (this.resourceUrl != null) {

                    this.$http.get(this.resourceUrl)
                    .then(function(data) {
                        return data.json()
                    })
                    .then(function(data) {
                        // Display new emoji data, or append.
                        if (this.fresh_search) {
                            this.emojis = [];
                        }
                        this.emojis.push(...data.results);

                        // if no results
                        if (this.emojis.length === 0) {
                            this.no_results_found = true
                        }
                        else {
                            this.no_results_found = false;
                        }

                        this.loading = false;
                        this.resourceUrl = data.next;
                    })
                    .catch(function(error) {
                        console.log('Error! Could not reach the API. ' + error);
                    })
                } 
            },

            debounceSearch: _.debounce(function() {
                // Debounce search feature to fetch new results based on search parameters.
                this.loading = true;
                let url = `http://localhost:8000/emoji?q=${this.search}&main_category=${this.main_category_query}&sub_category=${this.sub_category_query}`;
                this.resourceUrl = url;
                this.fresh_search = true;
                this.loadEmoji();
            }, 200)

        },

        computed: {
            // any_emojis: function() {
            //     if(this.emojis.length == 0) {
            //         return false;
            //     }
            //     // this.no_results_found = false;
            //     return true;
            // },

            selected_subcategories: function() {
                // Return the list of subcategories based on the selected main category.
                if (this.main_category_query) {
                    let selected_main_category = this.categories.find(obj => 
                        (obj.name == this.main_category_query)
                    )
                    this.sub_category_query = '';
                    return selected_main_category.subcategories
                }
            }
        },

        watch: {
            bottom() {
                if (this.bottom) {
                    this.fresh_search = false;
                    this.loadEmoji();

                    // If no more pages to fetch, dont show loader
                    if (this.resourceUrl === null){
                        this.loading = false;
                    }
                    else {
                        this.loading = true;
                    }
                    
                }
            }
        },

        created() {
            window.addEventListener('scroll', () => {
                this.bottom = this.bottomVisible();
            })
            this.loading = true;
            this.fresh_search = true;
            this.loadEmoji();
            this.loadCategories();

            // Watch for changes on three models.
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
.top-space {
    margin-top: 50px;
}

.bottom-space {
    margin-bottom: 50px;
}

.spinner {
    font-size: 7em;
    text-align: center;
}
</style>