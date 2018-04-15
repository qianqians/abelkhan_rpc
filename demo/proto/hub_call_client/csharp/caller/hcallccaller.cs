/*this caller file is codegen by abelkhan for c#*/
using System;
using System.Collections;
using System.IO;

namespace ntf
{
    public class hcallc
    {
        public hcallc()
        {
        }

        public hcallc_cliproxy get_client(string uuid)
        {
            return newhcallc_cliproxy(uuid);
        }

        public hcallc_cliproxy_multi get_multicast(Arraylist uuids)
        {
            return newhcallc_cliproxy_multi(uuids);
        }

        public hcallc_broadcast get_broadcast()
        {
            return newhcallc_broadcast(uuid);
        }

    }

    public class hcallc_cliproxy
    {
        private string uuid;

        public hcallc_cliproxy(string _uuid)
        {
            uuid = _uuid;
        }

        public void hcallc(String argv0)
        {
            ArrayList _argv = new ArrayList();
            _argv.Add(argv0);
            hub.hub.gates.call_client(uuid, "hcallc", "hcallc", _argv);
        }

    }

    public class hcallc_cliproxy_multi
    {
        private Arraylist uuids;

        public hcallc_cliproxy_multi(Arraylist _uuids)
        {
            uuids = _uuids;
        }

    }

    public class hcallc_broadcast
    {
        public hcallc_broadcast()
        {
            uuids = _uuids;
        }

    }

}
