import java.util.*;
import java.util.PriorityQueue;

public class Dijkstra {
    public static class Edge{
        int src,des,wt;
        public Edge(int s,int d,int w){
            this.src=s;
            this.des=d;
            this.wt=w;
        }
    }
    public static void createGraph(ArrayList<Edge>graph[]){
        for (int i = 0; i < graph.length; i++) {
            graph[i]= new ArrayList<>();
        }
        graph[0].add(new Edge(0, 1,2));
        graph[0].add(new Edge(0, 2,4));
        graph[1].add(new Edge(1, 2,1));
        graph[1].add(new Edge(1, 3,7));
        graph[2].add(new Edge(2, 4,3));
        graph[3].add(new Edge(3, 5,1));
        graph[4].add(new Edge(4, 3,2));
        graph[4].add(new Edge(4, 5,5));
        // graph[5].add(new Edge(5, 2));
    }
   public static class pair implements Comparable<pair>{
        int n,path;
        public pair(int n,int path){
            this.path=path;
            this.n=n;
        }
        @Override
        public int compareTo(pair p2) {
            return this.path-p2.path;
        }
    }

    public static void dijkstraAlgo(ArrayList<Edge> graph[],int src) {
        int dist[] = new int[graph.length];
        for (int i = 0; i < graph.length; i++) {
            if(i!=src){
                dist[i]=Integer.MAX_VALUE;
            }
        }
        boolean vis[]= new boolean[graph.length];
        PriorityQueue<pair> pq = new PriorityQueue<>();
        pq.add( new pair(src, 0));

        while (!pq.isEmpty()) {
            pair curr = pq.remove();
            if(!vis[curr.n]){
                vis[curr.n]=true;

                for (int i = 0; i < graph[curr.n].size(); i++) {
                    Edge e = graph[curr.n].get(i);
                    int u= e.src;
                    int v=e.des;
                    int wt=e.wt;
                    if(dist[u]+wt<dist[v]){
                        dist[v]=dist[u]+wt;
                        pq.add(new pair(v, dist[v]));
                    }
                }
            }
        }
        for (int i = 0; i < dist.length; i++) {
            System.out.print(dist[i]+" ");
        }
    }
    public static void main(String[] args) {
        ArrayList<Edge> graph[]= new ArrayList[6];
        createGraph(graph);
        dijkstraAlgo(graph, 0);
    }
}