import copy

def rogers_mc_file_names(datasets):
    file_list = ["/work/ast/cr67/mc/"+datasets+"/maus_output.root"]
    return file_list

def reco_file_names(run_number_list, maus, do_globals):
    file_list = []
    for run in run_number_list:
        run = str(run).rjust(5, '0')
        a_file = "/home/cr67/work/reco/"+maus+"/"+run+"/"+run+"_recon"
        if not do_globals:
            a_file += ".root"
        else:
            a_file += "_global.root"
        file_list.append(a_file)
    print file_list
    return file_list

def get_analysis(datasets, name, tof01_min_max, data_dir, p_bins, tkd_cut, do_globals):
    plot_dir = data_dir+"/plots_"+name+"/"
    plot_dir = plot_dir.replace(" ", "_")
    min_p = min([min(a_bin) for a_bin in p_bins])
    max_p = max([max(a_bin) for a_bin in p_bins])
    return {
            "plot_dir":plot_dir, # makedirs and then put plots in this directory. Removes any old plots there!!!
            "tof12_cut_low":32., # TOF12 cut lower bound
            "tof12_cut_high":39., # TOF12 cut upper bound
            "delta_tof01_lower":-1.0, # Delta TOF01 cut lower bound 
            "delta_tof01_upper":+1.5, # Delta TOF01 cut upper bound 
            "delta_tof12_lower":-5., # Delta TOF01 cut lower bound 
            "delta_tof12_upper":5., # Delta TOF01 cut upper bound 
            "tof01_cut_low":tof01_min_max[0], # TOF01 cut lower bound
            "tof01_cut_high":tof01_min_max[1], # TOF01 cut upper bound
            "p_bins":p_bins, # set of momentum bins; for now really it is just a lower and upper bound
            "p_tot_ds_low":tkd_cut[0], # downstream momentum cut lower bound
            "p_tot_ds_high":tkd_cut[1], # downstream momentum cut upper bound
            "reco_files":rogers_mc_file_names(datasets), # list of strings to be handed to glob
            "name":name, # appears on plots
            "color":4, # not used
            "pid":-13, # assume pid of tracks following TOF cut
            "pvalue_threshold":0.02, # minimum allowed pvalue for pvalue cut
            "chi2_threshold":4.0, # maximum allowed chi2/dof for chi2 cut
            "amplitude_source":"output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_base/amplitude/amplitude.json",
            "amplitude_systematic_reference":"output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_base/amplitude/amplitude.json",
            "amplitude_systematic_sources":{ # the first entry is the reference; others define deltas
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_pos_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_rot_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_scale_E1_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_scale_C_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_scale_E2_plus/amplitude/amplitude.json":1.,
                #"output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tku_density_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tkd_density_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tkd_scale_C_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tkd_scale_E2_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tkd_rot_plus/amplitude/amplitude.json":1.,
                "output/2017-02-Systematics/plots_Simulated_2017-2.7_6-140_lH2_empty_Systematics_tkd_pos_plus/amplitude/amplitude.json":1.,
            },
            "cov_fixed_us":None, #cov_us,
            "cov_fixed_ds":None, #cov_ds,
            "amplitude_algorithm":"binned",

            "field_uncertainty":0.02,
            "amplitude_chi2":False,
            "amplitude_mc":False,
            "weight_tof01_source":"output/2017-02_mc_weighting/plots_3-140-empty/tof01_weights",
            "weight_tof01_target":"output/2017-02_reco_weighting/plots_3-140-10069/tof01_weights",
            "weight_tof01_mode":"sample_using_distribution",
            "tracker_fiducial_radius":150.,

            "do_magnet_alignment":False,
            "do_amplitude":False,
            "do_extrapolation":False,
            "do_globals":do_globals,
            "do_mc":True,
            "do_plots":True,
            "do_cuts_plots":True,
            "do_tof01_weighting":False,
            "do_optics":False,
            "do_data_recorder":False,

        }

class Config(object):
    # location to which data and plots will be dumped following analysis
    info_file = "geometry_08681/Maus_Information.gdml"
    will_require_tof1 = True # require at least one TOF1 Space point to even load the data
    will_require_tof2 = False # require at least one TOF2 Space point to even load the data
    tk_station = 1 # load data from a particular tracker station
    tk_plane = 0
    # prerequisite for space point cut
    will_require_triplets = False #True # require triplet space points
    global_through_cuts = True
    upstream_cuts = { # Set to true to make data_plotter and amplitude_analysis use these cuts; False to ignore the cut
          "any_cut":None,
          "scifi_space_clusters":False,
          "scifi_space_points":False,
          "scifi_tracks_us":True,
          "scifi_nan_us":False,
          "scifi_track_points_us":False,
          "scifi_fiducial_us":True,
          "aperture_us":False,
          "pvalue_us":False,
          "chi2_us":True,
          "aperture_ds":False,
          "scifi_tracks_ds":False,
          "scifi_nan_ds":False,
          "scifi_track_points_ds":False,
          "scifi_fiducial_ds":False,
          "pvalue_ds":False,
          "chi2_ds":False,
          "tof01":True,
          "tof12":False,
          "p_tot_us":True,
          "p_tot_ds":False,
          "tof_0_sp":True,
          "tof_1_sp":True,
          "tof_2_sp":False,
          "upstream_aperture_cut":True,
          "downstream_aperture_cut":False,
          "delta_tof01":False, #True, #extrapolatedtof01 compared to recon tof01
          "delta_tof12":False, #extrapolatedtof12 compared to recon tof12
          "global_through_tof0":global_through_cuts,
          "global_through_tof1":False,
          "global_through_tku_tp":False,
          "global_through_tkd_tp":False,
          "global_through_tof2":False,
          "tof01_selection":False,
          "mc_muon_us":False,
          "mc_stations_us":False,
          "mc_scifi_fiducial_us":False,
          "mc_p_us":False,
          "mc_muon_ds":False,
          "mc_stations_ds":False,
          "mc_scifi_fiducial_ds":False,
    }
    downstream_cuts = copy.deepcopy(upstream_cuts)
    extrapolation_cuts = copy.deepcopy(upstream_cuts)
    mc_true_us_cuts = copy.deepcopy(upstream_cuts)
    for key, value in mc_true_us_cuts.iteritems():
        mc_true_us_cuts[key] = False
    mc_true_us_cuts["mc_muon_us"] = True
    mc_true_us_cuts["mc_stations_us"] = True
    mc_true_us_cuts["mc_scifi_fiducial_us"] = True
    mc_true_us_cuts["mc_p_us"] = True
    mc_true_ds_cuts = copy.deepcopy(mc_true_us_cuts)
    cut_report  = [[], []]
    cut_report[0] = ["hline", "all events", "hline",]
    cut_report[0] += ["tof_1_sp", "tof_0_sp", "scifi_tracks_us", "chi2_us", "scifi_fiducial_us", "hline",]
    cut_report[0] += ["tof01", "p_tot_us", "hline",]
    if global_through_cuts:
        cut_report[0] += ["global_through_tof0",]# "delta_tof01",]
    cut_report[0] += ["upstream_aperture_cut", "hline",]
    cut_report[0] += ["upstream_cut", "hline",]
    cut_report[1] = ["hline", "all events", "hline",]
    cut_report[1] += ["mc_stations_us", "mc_scifi_fiducial_us", "mc_p_us", "mc_muon_us", "hline",]
    cut_report[1] += ["mc_true_us_cut", "hline",]

    data_dir = "output/7469_v1"
    files = "*"
    analyses = []
    analyses.append(get_analysis("7469_v1/"+files, "Simulated 7469", [2.5, 3.], data_dir, [[195, 205]], [0, 1000], False))
    amplitude_bin_width = 5
    amplitude_max = 25

    required_trackers = [0, 1] # for space points
    required_number_of_track_points = 12 # doesnt do anything
    global_min_step_size = 1. # for extrapolation, set the extrapolation step size
    global_max_step_size = 100. # for extrapolation, set the extrapolation step size
    will_load_tk_space_points = True # determines whether data loader will attempt to load tracker space points
    will_load_tk_track_points = True # determines whether data loader will attempt to load tracker track points
    number_of_spills = 20 #100 # if set to an integer, limits the number of spills loaded for each sub-analysis
    # NOTE on memory usage: looks like about 10% + 5-10% per 200 spills with 16 GB RAM
    preanalysis_number_of_spills = 5 # number of spills to analyse during "pre-analysis"
    analysis_number_of_spills = 5 # number of spills to analyse during each "analysis" step
    momentum_from_tracker = True # i.e. not from TOFs
    time_from = "tof1"

    residuals_plots_nbins = 100 # used for track extrapolation plots
    extrapolation_does_apertures = True # set to True in order to include apertures in track extrapolation
    maus_verbose_level = 5

    magnet_alignment = {
        "n_events":10,
        "max_iterations":100,
        "resolution":1.,
    }
    # 
    tof0_offset = 0.18+25.4
    tof1_offset = 0.
    tof2_offset = -27.7

    # z position of central absorber (used for offsetting
    z_apertures = 0.
    # z position of detectors (used for track extrapolation) (z, name)
    # 13692: diffuser us edge
    # 13782: diffuser ds edge
    # 16639: lH2 window mount us (us edge)
    # 16710: lH2 window mount us (ds edge)
    # 16953.5: LiH centre
    # 17166: lH2 window mount ds (us edge)
    # 17242: lH2 window mount ds (ds edge)
    # 17585: SSU aperture
    # 18733: SSU He window
    tkd_pos = 18836.8+8.
    detectors = [
        (5287.2, None, "tof0"),
        (12929.6-25., None, "tof1_us"),
        (12929.6, None, "tof1"),
        (12929.6+25., None, "tof1_ds"),
        (13968.0, None, "tku_5"),
        (14318.0, None, "tku_4"),
        (14618.0, None, "tku_3"),
        (14867.0, None, "tku_2"),
        (15068.0, None, "tku_tp"),
        (tkd_pos+0., None, "tkd_tp"),
        (tkd_pos+200., None, "tkd_2"),
        (tkd_pos+450., None, "tkd_3"),
        (tkd_pos+750., None, "tkd_4"),
        (tkd_pos+1100., None, "tkd_5"),
        (21114.4, None, "tof2"),
        (21139.4, None, "tof2"),
        (21159.4, None, "tof2"),
        (21208., None, "tof2"),
        (21214.4, None, "tof2"),
        (21220.4, None, "tof2"),

    ]
    upstream_aperture_cut = {
        "global_through_virtual_diffuser_us":90.,
        "global_through_virtual_diffuser_ds":90.,
    }
    downstream_aperture_cut = {
        "global_through_virtual_lh2_us_window_flange_1":100.,
        "global_through_virtual_lh2_us_window_flange_2":100.,
        "global_through_virtual_absorber_centre":100.,
        "global_through_virtual_lh2_ds_window_flange_1":100.,
        "global_through_virtual_lh2_ds_window_flange_2":100.,
        "global_through_virtual_ssd_aperture":100.,
        "global_through_virtual_ssd_he":100.,
        "global_ds_virtual_ds_pry":100.,
    }

    virtual_detectors = [
        (12904., None, "virtual_tof1_us"),
        (12929., None, "virtual_tof1"),
        (12954., None, "virtual_tof1_ds"),
        (13205., None, "virtual_us_pry_us"),
        (13305., None, "virtual_us_pry_ds"),
        (13403., None, "virtual_tku_butterfly_us"),
        (13486., None, "virtual_tku_butterfly_ds"),
        (13578., None, "virtual_diffuser_shield"),
        (13698., None, "virtual_diffuser_us"),
        (13782., None, "virtual_diffuser_ds"),
        (16639., None, "virtual_lh2_us_window_flange_1"),
        (16710., None, "virtual_lh2_us_window_flange_2"),
        (16953.5, None, "virtual_absorber_centre"),
        (17166., None, "virtual_lh2_ds_window_flange_1"),
        (17242., None, "virtual_lh2_ds_window_flange_2"),
        (17585., None, "virtual_ssd_aperture"),
        (18733., None, "virtual_ssd_he"),
        (20447., None, "virtual_ds_pry"),
    ]
    plot_virtual_stations = [station for dummy, dummy, station in virtual_detectors]
    virtual_detectors += [(500.*i, None, "virtual_"+str(i)) for i in range(51)]
    virtual_detectors += [(z, None, "virtual_"+det) for z, dummy, det in detectors]
    virtual_detectors = sorted(virtual_detectors)
    for z, dummy, plane in virtual_detectors:
        print z, plane

    mc_plots = { # Used for virtual_cuts as well as plots
        "mc_stations" : { # one virtual plane for each tracker view; first must be tracker reference plane
            "tku":["mc_virtual_tku_tp", "mc_virtual_tku_2", "mc_virtual_tku_3", "mc_virtual_tku_4", "mc_virtual_tku_5",],
            "tkd":["mc_virtual_tkd_tp", "mc_virtual_tkd_2", "mc_virtual_tkd_3", "mc_virtual_tkd_4", "mc_virtual_tkd_5",],
        }
    }
    bz_tku = 3e-3
    bz_tkd = -2e-3
    z_afc = 16955.74
    # z position of apertures (z, maximum radius, name)
    # Notes from Jason: 209.6 to fixed flange
    # 282.5 to movable flange
    # what about tracker butterfly us and ds?
    apertures = sorted(
      [(-3325.74+z_afc, 100., "diffuser_us"),
       (-3276.74+z_afc, 100., "diffuser_mid"),
       (-3227.74+z_afc, 100., "diffuser_ds"),]+\
      [(float(z)+z_afc, 150., "tku_"+str(z)) for z in range(-2918, -1817, 100)]+\
      [(float(z)+z_afc, 150., "tkd_"+str(z)) for z in range(1818, 2919, 100)]+\
      [(float(z)+z_afc, 200., "pipe_"+str(z)) for z in range(-1800, 1801, 100)]+\
      [(+209.6+z_afc, 160., "afc_209.6")],
    )


