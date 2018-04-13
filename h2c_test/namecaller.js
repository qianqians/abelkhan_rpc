/*this ntf file is codegen by ablekhan for js*/

function name(hub_ptr){
    this.get_client = function(uuid){
        return new name_cliproxy(uuid, hub_ptr);
    }
    this.get_multicast = function(uuids){
        return new name_cliproxy_multi(uuids, hub_ptr);
    }
    this.get_broadcast = function(){
        return new name_broadcast(hub_ptr);
    }
}

function name_cliproxy(uuid, hub_ptr){
     this.uuid = uuid;

    this.func_test = function(argv0, argv1, argv2, argv3){
        hub_ptr.gates.call_client(uuid, "name", "func_test", argv0, argv1, argv2, argv3);
    }
}

function name_cliproxy_multi(uuids, hub_ptr){
    this.uuids = uuids;
    this.func_test1 = function(argv0, argv1, argv2){
        hub_ptr.gates.call_group_client(uuids, "name", "func_test1", argv0, argv1, argv2);
    }
}

function name_broadcast(hub_ptr){
    this.func_test2 = function(argv0, argv1, argv2){
        hub_ptr.gates.call_global_client("name", "func_test2", argv0, argv1, argv2);
    }
}

