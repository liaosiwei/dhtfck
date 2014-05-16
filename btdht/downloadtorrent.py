# coding=utf-8
import libtorrent as lt
import time
import sys

session_params = {
    'save_path': '/',
    'storage_mode': lt.storage_mode_t.storage_mode_sparse,
    'paused': True,
    'auto_managed': True,
    'duplicate_is_error': False
}


def getinfo(info):

    max_wait = 120
    ses = lt.session()
    ses.add_extension(lt.create_metadata_plugin)
    ses.add_extension(lt.create_ut_metadata_plugin)
    ses.add_extension(lt.create_ut_pex_plugin)
    ses.add_extension(lt.create_smart_ban_plugin)

    ses.add_dht_router("router.bittorrent.com", 6881)
    ses.add_dht_router("router.utorrent.com", 6881)
    ses.add_dht_router("router.bitcomet.com", 6881)
    ses.start_dht()
    ses.listen_on(6881, 6891)
    ses.start_lsd()

    magnet = "magnet:?xt=urn:btih:" + info
    torrent = lt.add_magnet_uri(ses, magnet, session_params)

    if ses.is_dht_running():
        print(ses.dht_state())
    wait_counter = 0
    torrent_info_received = True

    while not torrent.has_metadata():
        s = torrent.status()
        wait_counter += 1

        print("number of nodes and peer is " + str(ses.status().dht_nodes) + " " + str(s.num_peers))

        if wait_counter >= max_wait:
            torrent_info_received = False
            break
        print("waiting" + " " + str(wait_counter))
        time.sleep(1)

    if not torrent_info_received:
        return ""
    else:
        info = torrent.get_torrent_info()
        name = info.name()
        size = info.total_size() / 1024.0 / 1024.0
        print(name + " " + str(size))
        return name, size

if __name__ == "__main__":
    getinfo("4CDE5B50A8930315B479931F6872A3DB59575366")