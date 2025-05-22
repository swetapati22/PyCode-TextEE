import importlib

# Define the dataset mapper with module paths as strings
dataset_mapper = {
    "gsm8k": {
        "py_file": "evaluation_utils.eval_gsm8k",  # Python file as string
        "func_name": "eval_gsm8k"              # Function name as string
    },
    "ACE": {
        "py_file": "evaluation_utils.llama_events_scorer_OG",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "event_llama":{
        "py_file": "evaluation_utils.llama_events_scorer_OG",  # Python file as string
        "func_name": "micro_e2e_scores"
    },
    "wiki_events":{
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"
    },
    "event_llama_rq1":{
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"
    },
    "event_llama_rq3":{
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"
    },
    "event_llama_rq3_ds":{
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"
    },
    "wiki_events_rq3":{
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"
    },
    "ace_events_rq3": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "event_llama_rq4": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "event_llama_rq4_with_X_Y_split": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "event_llama_rq6": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "event_llama_rq6_with_X_Y_split": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "event_llama_rq3_1": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "event_llama_rq3_1_with_X_Y_split": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "load_event_llama_rq3": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "load_event_llama_rq3_with_X_Y_split": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "baseline_ace": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "baseline_wikievents": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"              # Function name as string
    },
    "baseline_maven": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_ed_scores"              # Function name as string
    },
    "load_multi_baseline_wo_guidelines": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "load_multi_baseline_wo_guidelines_new": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #From here is the individual dataset runs without guidelines
    "baseline_wo_guidelines_ace": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "baseline_wo_guidelines_maven": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_ed_scores"              # Function name as string
    },
    "baseline_wo_guidelines_wikievents": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"              # Function name as string
    },
    "inference_rq3_wikievents": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"              # Function name as string
    },
    "inference_rq3_wikievents_100": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"              # Function name as string
    },
    #did this wrong - I don't have this for my dataloader
    "inference_rq3_ace": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #From here is the individual dataset runs baseline_args_shuffle:
    "baseline_args_shuffle_ace": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "baseline_args_shuffle_maven": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_ed_scores"              # Function name as string
    },
    "baseline_args_shuffle_wikievents": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"              # Function name as string
    },
    #From here is the multi_baseline_args_shuffle:
    "load_multi_baseline_args_shuffle": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #Actual_baseline in multitask setting:
    "load_multi_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on entire dataset - dev with 1 event till we cover all using checkpoint from baseline
    "inference_dev1_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on entire dataset - dev with 4 event till we cover all using checkpoint frpm RQ3_70_30
    "inference_dev4_baseline_infered_rq3": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on entire dataset - dev with 4 event till we cover all using checkpoint frpm RQ3_100
    "inference_dev4_baseline_infered_rq3_100": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on entire dataset - dev with 4 event till we cover all using checkpoint frpm baseline
    "inference_dev4_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_only_baseline dataset:
    "inference_ace_dev1_ace_only_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on Maven dataset - dev with 1 event till we cover all using checkpoint from Maven_only_baseline dataset:
    "inference_maven_dev1_maven_only_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_ed_scores"              # Function name as string
    },
    #inference on wikievents dataset - dev with 1 event till we cover all using checkpoint from wikievents_only_baseline dataset:
    "inference_wikievents_dev1_wikievents_only_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"              # Function name as string
    },
    #Baseline_without_guidelines
    #inference on entire dataset - dev with 1 event till we cover all using checkpoint from baseline
    "inference_dev1_baseline_wo_guidelines": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_only_wo_guidelines_baseline dataset:
    "inference_ace_dev1_ace_only_wo_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on Maven dataset - dev with 1 event till we cover all using checkpoint from Maven_only_wo_guidelines_baseline dataset:
    "inference_maven_dev1_maven_only_wo_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_ed_scores"              # Function name as string
    },
    #inference on wikievents dataset - dev with 1 event till we cover all using checkpoint from wikievents_only_wo_guidelines_baseline dataset:
    "inference_wikievents_dev1_wikievents_only_wo_baseline": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_eae_scores"              # Function name as string
    },

    #INFERENCE_ON_NEGATIVE_SAMPLES:
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_Baseline trained w/o guideline w neg samples dataset:
    "inference_ace_dev1_ace_only_wo_guidelines_w_neg_samp": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_Baseline trained w guideline w neg samples dataset:
    "inference_ace_dev1_ace_only_w_guidelines_w_neg_samp": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },


    #ACE ONLY - trained on our data w/ human guideline and w/ neg samples (CP)
    "load_ACE_Only_w_guid_w_negativesample": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #ACE Only - trained on our data w/o human guideline and w/ neg samples (CP)
    "load_ACE_Only_wo_guid_w_negativesample": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },

    #NEW_TRAINING CE Only - trained on our data w/o human guideline and w/ neg samples (CP)
    "load_ACE_Only_wo_guid_w_negativesample_new": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },

    # testing
    "testing": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    # degreeACE
    "degree_ACE": {
        "py_file": "evaluation_utils.degree_ACE",  # Python file as string
        "func_name": "degree_ACE"              # Function name as string
    },
    # degreeACE
    "degree_ACE_total": {
        "py_file": "evaluation_utils.degree_ACE",  # Python file as string
        "func_name": "degree_ACE"              # Function name as string
    },


    ############GUIDELINE EXPERIMENTS############
    #Generated guidelines with only Positive examples:
    "guideline_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_P_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_P_wo_NS_full_dev_enum1": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #Generated guidelines with both Positive and 15 Negative examples:
    "guideline_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PN_wo_NS_full_dev_enum1": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    #Generated guidelines with both Positive and 15 Sibling examples:
    "guideline_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PS_wo_NS_full_dev_enum1": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PN_Adv": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PN_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PS_Adv": {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "guideline_PS_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",  # Python file as string
        "func_name": "micro_e2e_scores"              # Function name as string
    },
    "inference_ACE_Only_wo_guid_w_negativesample_new": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},

    ############MINI_GUIDELINE EXPERIMENTS############
    #Train100_no_guidelines:
    "miniguideline_train100_wo_guidelines_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_wo_guidelines_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_human_guidelines:
    "miniguideline_train100_Human_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_Human_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_Generated guidelines with only Positive examples:
    "miniguideline_train100_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_P_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_Generated guidelines with both Positive and 15 Negative examples:
    "miniguideline_train100_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_PN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "miniguideline_train100_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_PS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},


    #Testing_LLaMA3.2:
    "miniguideline_train100_wo_guidelines_w_NS_LLaMA3_2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},

    ############INFERENCE_MINI_GUIDELINE EXPERIMENTS############
    #Train100_no_guidelines:
    "inference_our_dev_miniguideline_train100_wo_guidelines_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "inference_our_dev_miniguideline_train100_wo_guidelines_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_human_guidelines:
    "inference_our_dev_miniguideline_train100_Human_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "inference_our_dev_miniguideline_train100_Human_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_Generated guidelines with only Positive examples:
    "inference_our_dev_miniguideline_train100_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "inference_our_dev_miniguideline_train100_P_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_Generated guidelines with both Positive and 15 Negative examples:
    "inference_our_dev_miniguideline_train100_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "inference_our_dev_miniguideline_train100_PN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_Generated guidelines with both Positive and 15 Sibling examples:
    "inference_our_dev_miniguideline_train100_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "inference_our_dev_miniguideline_train100_PS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train100_ consolidated adv random Generated guidelines:
    "miniguideline_train100_PN_Adv_w_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "miniguideline_train100_PN_Adv_wo_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train100_ consolidated adv sibling Generated guidelines:
    "miniguideline_train100_PS_Adv_w_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "miniguideline_train100_PS_Adv_wo_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    
    ############INFERENCE_onRICHERE__GUIDELINE EXPERIMENTS############
    "richere_test100_without_guideline_w_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_without_guideline_wo_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelineP_w_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelineP_wo_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePN_w_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePN_wo_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePS_w_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePS_wo_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePN_Adv_wo_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "richere_test100_guidelinePN_Adv_w_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},  
    "richere_test100_guidelinePS_Adv_wo_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "richere_test100_guidelinePS_Adv_w_NS_inference": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},

    ############Naming might be misleading but its INFERENCE_onFull_RICHERE_TestData_GUIDELINE EXPERIMENTS_Trained_on_Full_ACE############
    "richere_test100_without_guideline_w_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_without_guideline_wo_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},    
    "richere_test100_guidelineP_w_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelineP_wo_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePN_w_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePN_wo_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePS_w_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePS_wo_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePN_Adv_wo_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePN_Adv_w_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},   
    "richere_test100_guidelinePS_Adv_wo_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_test100_guidelinePS_Adv_w_NS_inference_full_test": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},       

    ############MINI2000_GUIDELINE EXPERIMENTS############
    #Train200_no_guidelines:
    "train2000_wo_guidelines_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "train2000_wo_guidelines_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train2000_human_guidelines:
    "train2000_Human_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "train2000_Human_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train2000_Generated guidelines with only Positive examples:
    "train2000_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "train2000_P_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train2000_Generated guidelines with both Positive and 15 Negative examples:
    "train2000_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "train2000_PN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train2000_Generated guidelines with both Positive and 15 Sibling examples:
    "train2000_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "train2000_PS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train100_Generated guidelines with consolidated random guidelines:
    "train2000_PN_Adv_w_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "train2000_PN_Adv_wo_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #Train100_Generated guidelines with consolidated sibling guidelines:
    "train2000_PS_Adv_w_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "train2000_PS_Adv_wo_NExample": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    ############Inference the full GUIDELINE EXPERIMENTS on new_full_coverage_dev_set############
    #no_guidelines:
    "infer_wo_guidelines_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "infer_wo_guidelines_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #human_guidelines:
    "infer_Human_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "infer_Human_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with only Positive examples:
    "infer_guideline_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "infer_guideline_P_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with both Positive and 15 Negative examples:
    "infer_guideline_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "infer_guideline_PN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with both Positive and 15 Sibling examples:
    "infer_guideline_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "infer_guideline_PS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines consolidated:
    "infer_guideline_PN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "infer_guideline_PN_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "infer_guideline_PS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "infer_guideline_PS_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    ############TEST on the full GUIDELINE EXPERIMENTS############
    #no_guidelines:
    "test_wo_guidelines_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test_wo_guidelines_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #human_guidelines:
    "test_Human_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test_Human_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with only Positive examples:
    "test_guideline_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test_guideline_P_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with both Positive and 15 Negative examples:
    "test_guideline_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test_guideline_PN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with both Positive and 15 Sibling examples:
    "test_guideline_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test_guideline_PS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines consolidated:
    "test_guideline_PN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "test_guideline_PN_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test_guideline_PS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test_guideline_PS_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    ############TEST on the 2000 GUIDELINE EXPERIMENTS############
    #no_guidelines:
    "test2000_wo_guidelines_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test2000_wo_guidelines_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #human_guidelines:
    "test2000_Human_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test2000_Human_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with only Positive examples:
    "test2000_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test2000_P_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with both Positive and 15 Negative examples:
    "test2000_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test2000_PN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines with both Positive and 15 Sibling examples:
    "test2000_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test2000_PS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Generated guidelines consolidated:
    "test2000_PN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "test2000_PN_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test2000_PS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "test2000_PS_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #######################################################RICHERE#######################################################

    #RICHERE 100 training samples
    "richere_train100_without_guideline_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_without_guideline_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelineP_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelineP_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePN_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePS_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePN_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePS_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train100_guidelinePS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #RICHERE 2000 training samples
    "richere_train2000_without_guideline_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_without_guideline_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelineP_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelineP_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePN_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePS_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePN_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePS_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train2000_guidelinePS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    #RICHERE full training samples
    "richere_train_without_guideline_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_without_guideline_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelineP_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelineP_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePN_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePS_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePN_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePS_Adv_w_NS" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "richere_train_guidelinePS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    ############MINI_GUIDELINE EXPERIMENTS _ 2 different samplings############
    #Train100_no_guidelines:
    "miniguideline_train100_wo_guidelines_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_wo_guidelines_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_human_guidelines:
    "miniguideline_train100_Human_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_Human_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_Generated guidelines with only Positive examples:
    "miniguideline_train100_P_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_P_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Train100_Generated guidelines with both Positive and 15 Negative examples:
    "miniguideline_train100_PN_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_PN_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer_unhasable_set_issue",
        "func_name": "micro_e2e_scores"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "miniguideline_train100_PS_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "miniguideline_train100_PS_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer_unhasable_set_issue",
        "func_name": "micro_e2e_scores"},
    #Train100_ consolidated adv random Generated guidelines:
    "miniguideline_train100_PN_Adv_w_NExample_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "miniguideline_train100_PN_Adv_w_NExample_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    #Train100_ consolidated adv sibling Generated guidelines:
    "miniguideline_train100_PS_Adv_w_NExample_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 
    "miniguideline_train100_PS_Adv_w_NExample_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"}, 

    ############ACE: test for 3 samples of Train100 for ACE############
    "test100_Human_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_Human_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_Human_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_P_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_P_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_P_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PN_Adv_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PN_Adv_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PN_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PN_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PN_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PS_Adv_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PS_Adv_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PS_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PS_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PS_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_PS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_wo_guidelines_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_wo_guidelines_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "test100_wo_guidelines_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },

    ############RICHERE: Train 3 more samples of Train100############
    "richere_train100_guidelineP_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelineP_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePN_Adv_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePN_Adv_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePN_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePN_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer_unhasable_set_issue",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePS_Adv_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePS_Adv_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePS_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_guidelinePS_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer_unhasable_set_issue",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_without_guideline_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_train100_without_guideline_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },

    ############RICHERE: test for 3 samples of Train100############
    "richere_test100_guidelineP_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelineP_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelineP_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelineP_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_Adv_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_Adv_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_Adv_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_Adv_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_guidelinePS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_without_guideline_w_NS_iter1": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_without_guideline_w_NS_iter2": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_without_guideline_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test100_without_guideline_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    ############RICHERE: test for 2000 Train############
    "richere_test2000_guidelineP_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelineP_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePN_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePS_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_guidelinePS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_without_guideline_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test2000_without_guideline_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },

    ############RICHERE: test for full Train############
    "richere_test_guidelineP_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelineP_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePN_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePN_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePN_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePN_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePS_Adv_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePS_Adv_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePS_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_guidelinePS_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_without_guideline_w_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },
    "richere_test_without_guideline_wo_NS": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"
    },

    ############FULL RICHERE TRAIN-> FULL TEST RICHERE, Test on the full ACE Test Data GUIDELINE EXPERIMENTS, Trained on full RICHERE Train Data############
    #no_guidelines:
    "test_wo_guidelines_w_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "test_wo_guidelines_wo_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #human_guidelines:
    "test_Human_w_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "test_Human_wo_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Generated guidelines with only Positive examples:
    "test_guideline_P_w_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "test_guideline_P_wo_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Generated guidelines with both Positive and 15 Negative examples:
    "test_guideline_PN_w_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "test_guideline_PN_wo_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "test_guideline_PS_w_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "test_guideline_PS_wo_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #Generated guidelines consolidated:
    "test_guideline_PN_Adv_wo_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "test_guideline_PN_Adv_w_NS_richeretrained" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "test_guideline_PS_Adv_wo_NS_richeretrained": {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
    "test_guideline_PS_Adv_w_NS_richeretrained" : {
        "py_file": "evaluation_utils.llama_events_scorer",
        "func_name": "micro_e2e_scores"},
}

def load_dataset_metrics(dataset_name):
    dataset_info = dataset_mapper.get(dataset_name)
    
    if dataset_info:
        module_name = dataset_info["py_file"]  # Get the module (Python file) as a string
        func_name = dataset_info["func_name"]  # Get the function name as a string
        
        # Dynamically import the module using importlib
        module = importlib.import_module(module_name)
        
        # Get the function from the module
        func = getattr(module, func_name)
        
        # Call the function
        return func  # Assuming the function takes no arguments
    else:
        raise ValueError(f"Dataset {dataset_name} not found in dataset_mapper.")
