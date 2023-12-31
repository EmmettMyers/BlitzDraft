import Vue from "vue";
import { HttpHeaders, HttpOptions, HttpResponse, $http, $resource } from "./vue_resource";

declare module "vue/types/options" {
    interface ComponentOptions<V extends Vue> {
        http?: (HttpOptions & { headers?: HttpHeaders } & { [key: string]: any })
    }
}

declare module "vue/types/vue" {
    interface Vue {
        $http: {
            (options: HttpOptions): PromiseLike<HttpResponse>;
            get: $http;
            post: $http;
            put: $http;
            patch: $http;
            delete: $http;
            jsonp: $http;
        };
        $resource: $resource;
    }
}

interface Player {
    pos: string;
    name: string;
    stats: number[];
    image?: string;
}