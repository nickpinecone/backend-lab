<script>
    import { onMount } from "svelte";
    import * as signalR from "@microsoft/signalr";

    let students = 0;

    onMount(async () => {
        let result = await fetch("http://localhost:5000/students");
        let text = await result.text();

        students = Number(text);

        var connection = new signalR.HubConnectionBuilder()
            .withUrl("http://localhost:5002/signal", {
                transport: signalR.HttpTransportType.ServerSentEvents,
                withCredentials: false,
            })
            .build();

        connection.on("ReceiveMessage", function (count) {
            students = count;
        });

        connection.start();
    });
</script>

<main>
    <table>
        <tr>
            <th>Студенты</th>
            <!-- <th>Курсы</th> -->
        </tr>
        <tr>
            <td>{students}</td>
            <!-- <td>{courses}</td> -->
        </tr>
    </table>
</main>

<style>
    th,
    td {
        padding: 1rem;
        text-align: center;
    }
</style>
