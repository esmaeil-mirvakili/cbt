class Cluster(object):
    def __init__(self, config):
        self.config = config
        base_tmp = config.get('tmp_dir', '/tmp/cbt')
        self.mnt_dir = config.get('mnt_dir', "%s/%s" % (base_tmp, 'mnt'))
        self.tmp_dir = "%s/%s" % (base_tmp, config.get('clusterid'))
        self.archive_dir = "%s/%s" % (config.get('archive_dir'), config.get('clusterid'))

    def get_mnt_dir(self):
        return self.mnt_dir

    def getclass(self):
        return self.__class__.__name__

    def initialize(self):
        pass

    def cleanup(self):
        pass

    def pre_bench(self):
        pass

    def post_bench(self):
        pass

    def __str__(self):
        return str(self.config)
