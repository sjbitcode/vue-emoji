<template>
    <div id="emojis">
        <div id="category" v-for="emoji_category, emoji_category_text in emojis">
            <h1>{{ emoji_category_text }}</h1>
            
            <div id="emoji" v-for="val, key in emoji_category">
                <span @click="copy(key)" v-tooltip.top="{content: val, delay: 0}">{{ key }}</span>
            </div>
            
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

            }
        },

        methods: {
            copy: function(emoji) {
              this.$clipboard(emoji);
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