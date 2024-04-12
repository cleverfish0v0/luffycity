import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'

//这是按照需求加载element组件的支持
import Components from 'unplugin-vue-components/vite'
import {ElementPlusResolver} from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        //按照需求加载
        Components({
            resolvers: [ElementPlusResolver()],
        }),
    ]
});