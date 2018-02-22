<template>
    <div id="emojis">

        <input type="text" v-model="search" placeholder="search">
        <div v-for="emoji, alias in filtered_emojis">
            <span>{{ emoji }} - {{ alias }}</span>
        </div>
        
    </div>
</template>


<script>
    export default {
        props: {

            emojis: {
                type: Object,
                required: true
            }
        },

        data() {
            return {
                search: ''
            }
        },

        methods: {
            copy: function(emoji) {
              this.$clipboard(emoji);
            }
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
            }
        }
    }
</script>


<style>

    #emojis {
        width: 100%;
        max-width: 1200px;
        margin: 40px auto;
        padding: 0 20px;
        box-sizing: border-box;
    }

    #category {
        display: flex;
        flex-wrap: wrap;
        list-style-type: none;
        padding: 0;
    }

    #emoji {
        flex-grow: 1;
        text-align: center;
        padding: 20px;
        margin: 10px;
        font-size:5rem;
    }
</style>