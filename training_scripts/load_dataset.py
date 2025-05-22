import importlib

# Define the dataset mapper with module paths as strings
dataset_mapper = {
    "gsm8k": {
        "py_file": "dataset_utils.load_gsm8k",  # Python file as string
        "func_name": "load_gsm8k"},             # Function name as string
    "ACE": {
        "py_file": "dataset_utils.load_ACE",
        "func_name": "load_ACE"},
    "event_llama": {
        "py_file": "dataset_utils.load_EventLLaMA",
        "func_name": "load_LLaMAEvents"},
    "wiki_events": {
        "py_file": "dataset_utils.load_wikievents",
        "func_name": "load_wikievents"},
    "event_llama_rq1": {
        "py_file": "dataset_utils.load_event_llama_rq1",
        "func_name": "load_event_llama_rq1"},
    "event_llama_rq3": {
        "py_file": "dataset_utils.load_event_llama_rq3",
        "func_name": "load_event_llama_rq3"},
    "event_llama_rq3_ds": {
        "py_file": "dataset_utils.load_event_llama_rq3_ds",
        "func_name": "load_event_llama_rq3_ds"},
    "wiki_events_rq3": {
        "py_file": "dataset_utils.load_wiki_events_rq3",
        "func_name": "load_wiki_events_rq3"},
    "ace_events_rq3": {
        "py_file": "dataset_utils.load_ace_events_rq3",
        "func_name": "load_ace_events_rq3"},
    "event_llama_rq4": {
        "py_file": "dataset_utils.load_event_llama_rq4",
        "func_name": "load_event_llama_rq4"},
    "event_llama_rq4_with_X_Y_split": {
        "py_file": "dataset_utils.load_event_llama_rq4_with_X_Y_split",
        "func_name": "load_event_llama_rq4_with_X_Y_split"},
    "event_llama_rq6": {
        "py_file": "dataset_utils.load_event_llama_rq6",
        "func_name": "load_event_llama_rq6"},
    "event_llama_rq6_with_X_Y_split": {
        "py_file": "dataset_utils.load_event_llama_rq6_with_X_Y_split",
        "func_name": "load_event_llama_rq6_with_X_Y_split"},
    "event_llama_rq3_1": {
        "py_file": "dataset_utils.load_event_llama_rq3_1",
        "func_name": "load_event_llama_rq3_1"},
    "event_llama_rq3_1_with_X_Y_split": {
        "py_file": "dataset_utils.load_event_llama_rq3_1_with_X_Y_split",
        "func_name": "load_event_llama_rq3_1_with_X_Y_split"},
    #inference on entire dataset
    "load_event_llama_rq3": {
        "py_file": "dataset_utils.load_event_llama_rq3",
        "func_name": "load_event_llama_rq3"},
    "load_event_llama_rq3_with_X_Y_split": {
        "py_file": "dataset_utils.load_event_llama_rq3_with_X_Y_split",
        "func_name": "load_event_llama_rq3_with_X_Y_split"},
    #wikievents_on_X_Y_split_checkpoint
    "inference_rq3_wikievents": {
        "py_file": "dataset_utils.inference_rq3_wikievents",
        "func_name": "inference_rq3_wikievents"},
    #wikievents_on_X_Y_split_checkpoint
    "inference_rq3_wikievents_100": {
        "py_file": "dataset_utils.inference_rq3_wikievents_100",
        "func_name": "inference_rq3_wikievents_100"},
    #ACE_
    "inference_rq3_ace": {
        "py_file": "dataset_utils.inference_rq3_ace",
        "func_name": "inference_rq3_ace"},
    #baselines_individual
    "baseline_ace": {
        "py_file": "dataset_utils.baseline_ace",
        "func_name": "baseline_ace"},
    "baseline_wikievents": {
        "py_file": "dataset_utils.baseline_wikievents",
        "func_name": "baseline_wikievents"},
    "baseline_maven": {
        "py_file": "dataset_utils.baseline_maven",
        "func_name": "baseline_maven"},
    #Multi_without guidelines
    "load_multi_baseline_wo_guidelines": {
        "py_file": "dataset_utils.load_multi_baseline_wo_guidelines",
        "func_name": "load_multi_baseline_wo_guidelines"},
    "load_multi_baseline_wo_guidelines_new": {
        "py_file": "dataset_utils.load_multi_baseline_wo_guidelines_new",
        "func_name": "load_multi_baseline_wo_guidelines_new"},
    #baselines_individual without guidelines
    "baseline_wo_guidelines_ace": {
        "py_file": "dataset_utils.baseline_wo_guidelines_ace",
        "func_name": "baseline_wo_guidelines_ace"},
    "baseline_wo_guidelines_wikievents": {
        "py_file": "dataset_utils.baseline_wo_guidelines_wikievents",
        "func_name": "baseline_wo_guidelines_wikievents"},
    "baseline_wo_guidelines_maven": {
        "py_file": "dataset_utils.baseline_wo_guidelines_maven",
        "func_name": "baseline_wo_guidelines_maven"},
    #Baseline_args_shuffle
    "load_multi_baseline_args_shuffle": {
        "py_file": "dataset_utils.load_multi_baseline_args_shuffle",
        "func_name": "load_multi_baseline_args_shuffle"},
    #baselines_individual_args_shuffle 
    "baseline_args_shuffle_ace": {
        "py_file": "dataset_utils.baseline_args_shuffle_ace",
        "func_name": "baseline_args_shuffle_ace"},
    "baseline_args_shuffle_wikievents": {
        "py_file": "dataset_utils.baseline_args_shuffle_wikievents",
        "func_name": "baseline_args_shuffle_wikievents"},
    "baseline_args_shuffle_maven": {
        "py_file": "dataset_utils.baseline_args_shuffle_maven",
        "func_name": "baseline_args_shuffle_maven"},
    #Actual_baseline in multitask setting:
    "load_multi_baseline":{
        "py_file": "dataset_utils.load_multi_baseline",
        "func_name": "load_multi_baseline"},
    #inference on entire dataset - dev with 1 event till we cover all using checkpoint from baseline
    "inference_dev1_baseline": {
        "py_file": "dataset_utils.inference_dev1_baseline",
        "func_name": "inference_dev1_baseline"},
    #inference on entire dataset - dev with 4 event till we cover all using checkpoint frpm RQ3_with_X_Y
    "inference_dev4_baseline_infered_rq3": {
        "py_file": "dataset_utils.inference_dev4_baseline_infered_rq3",
        "func_name": "inference_dev4_baseline_infered_rq3"},
    #inference on entire dataset - dev with 4 event till we cover all using checkpoint frpm RQ3_100
    "inference_dev4_baseline_infered_rq3_100": {
        "py_file": "dataset_utils.inference_dev4_baseline_infered_rq3_100",
        "func_name": "inference_dev4_baseline_infered_rq3_100"},
    #inference on entire dataset - dev with 4 event till we cover all using checkpoint frpm baseline
    "inference_dev4_baseline": {
        "py_file": "dataset_utils.inference_dev4_baseline",
        "func_name": "inference_dev4_baseline"},
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_only_baseline dataset:
    "inference_ace_dev1_ace_only_baseline": {
        "py_file": "dataset_utils.inference_ace_dev1_ace_only_baseline",
        "func_name": "inference_ace_dev1_ace_only_baseline"},
    #inference on Maven dataset - dev with 1 event till we cover all using checkpoint from Maven_only_baseline dataset:
    "inference_maven_dev1_maven_only_baseline": {
        "py_file": "dataset_utils.inference_maven_dev1_maven_only_baseline",
        "func_name": "inference_maven_dev1_maven_only_baseline"},
    #inference on wikievents dataset - dev with 1 event till we cover all using checkpoint from wikievents_only_baseline dataset:
    "inference_wikievents_dev1_wikievents_only_baseline": {
        "py_file": "dataset_utils.inference_wikievents_dev1_wikievents_only_baseline",
        "func_name": "inference_wikievents_dev1_wikievents_only_baseline"},
    # You can add more datasets as needed, event_llama_rq1 
    #Baseline without guidelines
    #inference on entire dataset - dev with 1 event till we cover all using checkpoint from baseline
    "inference_dev1_baseline_wo_guidelines": {
        "py_file": "dataset_utils.inference_dev1_baseline_wo_guidelines",
        "func_name": "inference_dev1_baseline_wo_guidelines"},
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_only_wo_guidelines_baseline dataset:
    "inference_ace_dev1_ace_only_wo_baseline": {
        "py_file": "dataset_utils.inference_ace_dev1_ace_only_wo_baseline",
        "func_name": "inference_ace_dev1_ace_only_wo_baseline"},
    #inference on Maven dataset - dev with 1 event till we cover all using checkpoint from Maven_only_wo_guidelines_baseline dataset:
    "inference_maven_dev1_maven_only_wo_baseline": {
        "py_file": "dataset_utils.inference_ace_dev1_ace_only_wo_baseline",
        "func_name": "inference_ace_dev1_ace_only_wo_baseline"},
    #inference on wikievents dataset - dev with 1 event till we cover all using checkpoint from wikievents_only_wo_guidelines_baseline dataset:
    "inference_wikievents_dev1_wikievents_only_wo_baseline": {
        "py_file": "dataset_utils.inference_ace_dev1_ace_only_wo_baseline",
        "func_name": "inference_ace_dev1_ace_only_wo_baseline"},

    #WITH NEGATIVE SAMPLES:
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_Baseline trained w/o guideline w neg samples dataset:
    "inference_ace_dev1_ace_only_wo_guidelines_w_neg_samp": {
        "py_file": "dataset_utils.inference_ace_dev1_ace_only_wo_guidelines_w_neg_samp",
        "func_name": "inference_ace_dev1_ace_only_wo_guidelines_w_neg_samp"},
    #inference on ACE dataset - dev with 1 event till we cover all using checkpoint from ACE_Baseline trained w guideline w neg samples dataset:
    "inference_ace_dev1_ace_only_w_guidelines_w_neg_samp": {
        "py_file": "dataset_utils.inference_ace_dev1_ace_only_w_guidelines_w_neg_samp",
        "func_name": "inference_ace_dev1_ace_only_w_guidelines_w_neg_samp"},

    #ACE ONLY - trained on our data w/ human guideline and w/ neg samples (CP)
    "load_ACE_Only_w_guid_w_negativesample": {
        "py_file": "dataset_utils.load_ACE_Only_w_guid_w_negativesample",
        "func_name": "load_ACE_Only_w_guid_w_negativesample"},
    #ACE Only - trained on our data w/o human guideline and w/ neg samples (CP)
    "load_ACE_Only_wo_guid_w_negativesample": {
        "py_file": "dataset_utils.load_ACE_Only_wo_guid_w_negativesample",
        "func_name": "load_ACE_Only_wo_guid_w_negativesample"},
    #ACE Only - trained on our data w/o human guideline and w/ neg samples (CP)
    "load_ACE_Only_wo_guid_w_negativesample_new": {
        "py_file": "dataset_utils.load_ACE_Only_wo_guid_w_negativesample_new",
        "func_name": "load_ACE_Only_wo_guid_w_negativesample_new"},

    #Degree from TEXTEE (NLI)
   "degree_ACE":{
        "py_file": "dataset_utils.degree_ACE",
        "func_name": "degree_ACE"},
    #degree_ACE_total:
    "degree_ACE_total":{
        "py_file": "dataset_utils.degree_ACE_total",
        "func_name": "degree_ACE_total"},
    #Code Understanding:
    "testing": {
        "py_file": "dataset_utils.testing",
        "func_name": "testing"},

    ############GUIDELINE EXPERIMENTS############
    #Generated guidelines with only Positive examples:
    "guideline_P_w_NS": {
        "py_file": "dataset_utils.guideline_P_w_NS",
        "func_name": "guideline_P_w_NS"},
    "guideline_P_wo_NS": {
        "py_file": "dataset_utils.guideline_P_wo_NS",
        "func_name": "guideline_P_wo_NS"},
    "guideline_P_wo_NS_full_dev_enum1": {
        "py_file": "dataset_utils.guideline_P_wo_NS_full_dev_enum1",
        "func_name": "guideline_P_wo_NS_full_dev_enum1"},
    #Generated guidelines with both Positive and 15 Negative examples:
    "guideline_PN_w_NS": {
        "py_file": "dataset_utils.guideline_PN_w_NS",
        "func_name": "guideline_PN_w_NS"},
    "guideline_PN_wo_NS": {
        "py_file": "dataset_utils.guideline_PN_wo_NS",
        "func_name": "guideline_PN_wo_NS"},
    "guideline_PN_wo_NS_full_dev_enum1": {
        "py_file": "dataset_utils.guideline_PN_wo_NS_full_dev_enum1",
        "func_name": "guideline_PN_wo_NS_full_dev_enum1"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "guideline_PS_w_NS": {
        "py_file": "dataset_utils.guideline_PS_w_NS",
        "func_name": "guideline_PS_w_NS"},
    "guideline_PS_wo_NS": {
        "py_file": "dataset_utils.guideline_PS_wo_NS",
        "func_name": "guideline_PS_wo_NS"},
    "guideline_PS_wo_NS_full_dev_enum1": {
        "py_file": "dataset_utils.guideline_PS_wo_NS_full_dev_enum1",
        "func_name": "guideline_PS_wo_NS_full_dev_enum1"},

    #Generated guidelines consolidated:
    "guideline_PN_Adv": {
        "py_file": "dataset_utils.guideline_PN_Adv",
        "func_name": "guideline_PN_Adv"},
    "guideline_PN_Adv_w_NS" : {
        "py_file": "dataset_utils.guideline_PN_Adv_w_NS",
        "func_name": "guideline_PN_Adv_w_NS"},
    "guideline_PS_Adv": {
        "py_file": "dataset_utils.guideline_PS_Adv",
        "func_name": "guideline_PS_Adv"},
    "guideline_PS_Adv_w_NS" : {
        "py_file": "dataset_utils.guideline_PS_Adv_w_NS",
        "func_name": "guideline_PS_Adv_w_NS"},

    "inference_ACE_Only_wo_guid_w_negativesample_new": {
        "py_file": "dataset_utils.inference_ACE_Only_wo_guid_w_negativesample_new",
        "func_name": "inference_ACE_Only_wo_guid_w_negativesample_new"},



    ############MINI_GUIDELINE EXPERIMENTS############
    #Train100_no_guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/baseline_without_guidelines/final_baseline_wo_guideline_3data/ace05-en/PA_train_100_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/baseline_without_guidelines/final_baseline_wo_guideline_3data/ace05-en/PA_dev_100_final.json
    "miniguideline_train100_wo_guidelines_w_NS": {
        "py_file": "dataset_utils.miniguideline_train100_wo_guidelines_w_NS",
        "func_name": "miniguideline_train100_wo_guidelines_w_NS"},
    "miniguideline_train100_wo_guidelines_wo_NS": {
        "py_file": "dataset_utils.miniguideline_train100_wo_guidelines_wo_NS",
        "func_name": "miniguideline_train100_wo_guidelines_wo_NS"},
    #Train100_human_guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_dev_final.json
    "miniguideline_train100_Human_w_NS": {
        "py_file": "dataset_utils.miniguideline_train100_Human_w_NS",
        "func_name": "miniguideline_train100_Human_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_dev_final.json
    "miniguideline_train100_Human_wo_NS": {
        "py_file": "dataset_utils.miniguideline_train100_Human_wo_NS",
        "func_name": "miniguideline_train100_Human_wo_NS"},
    #Train100_Generated guidelines with only Positive examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_dev_final.json
    "miniguideline_train100_P_w_NS": {
        "py_file": "dataset_utils.miniguideline_train100_P_w_NS",
        "func_name": "miniguideline_train100_P_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_dev_final.json
    "miniguideline_train100_P_wo_NS": {
        "py_file": "dataset_utils.miniguideline_train100_P_wo_NS",
        "func_name": "miniguideline_train100_P_wo_NS"},
    #Train100_Generated guidelines with both Positive and 15 Negative examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_dev_final.json
    "miniguideline_train100_PN_w_NS": {
        "py_file": "dataset_utils.miniguideline_train100_PN_w_NS",
        "func_name": "miniguideline_train100_PN_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_dev_final.json
    "miniguideline_train100_PN_wo_NS": {
        "py_file": "dataset_utils.miniguideline_train100_PN_wo_NS",
        "func_name": "miniguideline_train100_PN_wo_NS"},
    #Train100_Generated guidelines with both Positive and 15 Sibling examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_dev_final.json
    "miniguideline_train100_PS_w_NS": {
        "py_file": "dataset_utils.miniguideline_train100_PS_w_NS",
        "func_name": "miniguideline_train100_PS_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_dev_final.json
    "miniguideline_train100_PS_wo_NS": {
        "py_file": "dataset_utils.miniguideline_train100_PS_wo_NS",
        "func_name": "miniguideline_train100_PS_wo_NS"}, 

    #Train100_ consolidated adv random Generated guidelines:
    "miniguideline_train100_PN_Adv_w_NExample": {
        "py_file": "dataset_utils.miniguideline_train100_PN_Adv_w_NExample",
        "func_name": "miniguideline_train100_PN_Adv_w_NExample"},
    "miniguideline_train100_PN_Adv_wo_NExample": {
        "py_file": "dataset_utils.miniguideline_train100_PN_Adv_wo_NExample",
        "func_name": "miniguideline_train100_PN_Adv_wo_NExample"}, 

    #Train100_ consolidated adv sibling Generated guidelines:
    "miniguideline_train100_PS_Adv_w_NExample": {
        "py_file": "dataset_utils.miniguideline_train100_PS_Adv_w_NExample",
        "func_name": "miniguideline_train100_PS_Adv_w_NExample"},
    "miniguideline_train100_PS_Adv_wo_NExample": {
        "py_file": "dataset_utils.miniguideline_train100_PS_Adv_wo_NExample",
        "func_name": "miniguideline_train100_PS_Adv_wo_NExample"}, 
    
    ############INFERENCE_MINI_GUIDELINE EXPERIMENTS############
    #Train100_no_guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/baseline_without_guidelines/final_baseline_wo_guideline_3data/ace05-en/PA_train_100_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/baseline_without_guidelines/final_baseline_wo_guideline_3data/ace05-en/PA_dev_100_final.json
     # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/baseline_without_guidelines/final_baseline_wo_guideline_3data/ace05-en/dev_100_same_ids_final.json
    "inference_our_dev_miniguideline_train100_wo_guidelines_w_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_wo_guidelines_w_NS",
        "func_name": "inference_our_dev_miniguideline_train100_wo_guidelines_w_NS"},
    "inference_our_dev_miniguideline_train100_wo_guidelines_wo_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_wo_guidelines_wo_NS",
        "func_name": "inference_our_dev_miniguideline_train100_wo_guidelines_wo_NS"},
    #Train100_human_guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_Human_w_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_Human_w_NS",
        "func_name": "inference_our_dev_miniguideline_train100_Human_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_Human_wo_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_Human_wo_NS",
        "func_name": "inference_our_dev_miniguideline_train100_Human_wo_NS"},
    #Train100_Generated guidelines with only Positive examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_P_w_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_P_w_NS",
        "func_name": "inference_our_dev_miniguideline_train100_P_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_P_wo_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_P_wo_NS",
        "func_name": "inference_our_dev_miniguideline_train100_P_wo_NS"},
    #Train100_Generated guidelines with both Positive and 15 Negative examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_PN_w_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_PN_w_NS",
        "func_name": "inference_our_dev_miniguideline_train100_PN_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_PN_wo_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_PN_wo_NS",
        "func_name": "inference_our_dev_miniguideline_train100_PN_wo_NS"},
    #Train100_Generated guidelines with both Positive and 15 Sibling examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_train_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_PS_w_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_PS_w_NS",
        "func_name": "inference_our_dev_miniguideline_train100_PS_w_NS"},
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_train.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_dev_final.json
    "inference_our_dev_miniguideline_train100_PS_wo_NS": {
        "py_file": "dataset_utils.inference_our_dev_miniguideline_train100_PS_wo_NS",
        "func_name": "inference_our_dev_miniguideline_train100_PS_wo_NS"},   

    ############INFERENCE_onRICHERE__GUIDELINE EXPERIMENTS############
    "richere_test100_without_guideline_w_NS_inference": {
        "py_file": "dataset_utils.richere_test100_without_guideline_w_NS_inference",
        "func_name": "richere_test100_without_guideline_w_NS_inference"}, 
    "richere_test100_without_guideline_wo_NS_inference": {
        "py_file": "dataset_utils.richere_test100_without_guideline_wo_NS_inference",
        "func_name": "richere_test100_without_guideline_wo_NS_inference"},     
    "richere_test100_guidelineP_w_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelineP_w_NS_inference",
        "func_name": "richere_test100_guidelineP_w_NS_inference"},  
    "richere_test100_guidelineP_wo_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelineP_wo_NS_inference",
        "func_name": "richere_test100_guidelineP_wo_NS_inference"},
    "richere_test100_guidelinePN_w_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_w_NS_inference",
        "func_name": "richere_test100_guidelinePN_w_NS_inference"}, 
    "richere_test100_guidelinePN_wo_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_wo_NS_inference",
        "func_name": "richere_test100_guidelinePN_wo_NS_inference"},
    "richere_test100_guidelinePS_w_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_w_NS_inference",
        "func_name": "richere_test100_guidelinePS_w_NS_inference"},
    "richere_test100_guidelinePS_wo_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_wo_NS_inference",
        "func_name": "richere_test100_guidelinePS_wo_NS_inference"},
    "richere_test100_guidelinePN_Adv_wo_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_wo_NS_inference",
        "func_name": "richere_test100_guidelinePN_Adv_wo_NS_inference"},
    "richere_test100_guidelinePN_Adv_w_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_w_NS_inference",
        "func_name": "richere_test100_guidelinePN_Adv_w_NS_inference"},     
    "richere_test100_guidelinePS_Adv_wo_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_wo_NS_inference",
        "func_name": "richere_test100_guidelinePS_Adv_wo_NS_inference"},
    "richere_test100_guidelinePS_Adv_w_NS_inference": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_w_NS_inference",
        "func_name": "richere_test100_guidelinePS_Adv_w_NS_inference"},

    ############Naming might be misleading but its INFERENCE_onFull_RICHERE_TestData_GUIDELINE EXPERIMENTS_Trained_on_Full_ACE############
    "richere_test100_without_guideline_w_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_without_guideline_w_NS_inference_full_test",
        "func_name": "richere_test100_without_guideline_w_NS_inference_full_test"}, 
    "richere_test100_without_guideline_wo_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_without_guideline_wo_NS_inference_full_test",
        "func_name": "richere_test100_without_guideline_wo_NS_inference_full_test"},     
    "richere_test100_guidelineP_w_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelineP_w_NS_inference_full_test",
        "func_name": "richere_test100_guidelineP_w_NS_inference_full_test"},  
    "richere_test100_guidelineP_wo_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelineP_wo_NS_inference_full_test",
        "func_name": "richere_test100_guidelineP_wo_NS_inference_full_test"},
    "richere_test100_guidelinePN_w_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_w_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePN_w_NS_inference_full_test"}, 
    "richere_test100_guidelinePN_wo_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_wo_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePN_wo_NS_inference_full_test"},
    "richere_test100_guidelinePS_w_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_w_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePS_w_NS_inference_full_test"},
    "richere_test100_guidelinePS_wo_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_wo_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePS_wo_NS_inference_full_test"},
    "richere_test100_guidelinePN_Adv_wo_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_wo_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePN_Adv_wo_NS_inference_full_test"},
    "richere_test100_guidelinePN_Adv_w_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_w_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePN_Adv_w_NS_inference_full_test"},     
    "richere_test100_guidelinePS_Adv_wo_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_wo_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePS_Adv_wo_NS_inference_full_test"},
    "richere_test100_guidelinePS_Adv_w_NS_inference_full_test": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_w_NS_inference_full_test",
        "func_name": "richere_test100_guidelinePS_Adv_w_NS_inference_full_test"},      

    ############MINI2000_GUIDELINE EXPERIMENTS############
    #Train200_no_guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/baseline_without_guidelines/final_baseline_wo_guideline_3data/ace05-en/PA_train_2000_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/baseline_without_guidelines/final_baseline_wo_guideline_3data/ace05-en/PA_dev_100_final.json
    "train2000_wo_guidelines_w_NS": {
        "py_file": "dataset_utils.train2000_wo_guidelines_w_NS",
        "func_name": "train2000_wo_guidelines_w_NS"},
    "train2000_wo_guidelines_wo_NS": {
        "py_file": "dataset_utils.train2000_wo_guidelines_wo_NS",
        "func_name": "train2000_wo_guidelines_wo_NS"},

    #Train2000_human_guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_train_2000_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/modified_baseline/inference_3_datasets/ace05-en/PA_100_dev_final.json
    "train2000_Human_w_NS": {
        "py_file": "dataset_utils.train2000_Human_w_NS",
        "func_name": "train2000_Human_w_NS"},
    "train2000_Human_wo_NS": {
        "py_file": "dataset_utils.train2000_Human_wo_NS",
        "func_name": "train2000_Human_wo_NS"},

    #Train2000_Generated guidelines with only Positive examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_train_2000_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_guidelines_w_pos_examples/final_data_split/PA_100_dev_final.json
    "train2000_P_w_NS": {
        "py_file": "dataset_utils.train2000_P_w_NS",
        "func_name": "train2000_P_w_NS"},
    "train2000_P_wo_NS": {
        "py_file": "dataset_utils.train2000_P_wo_NS",
        "func_name": "train2000_P_wo_NS"},

    #Train2000_Generated guidelines with both Positive and 15 Negative examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_train_2000_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_examples/final_data_split/PA_100_dev_final.json
    "train2000_PN_w_NS": {
        "py_file": "dataset_utils.train2000_PN_w_NS",
        "func_name": "train2000_PN_w_NS"},
    "train2000_PN_wo_NS": {
        "py_file": "dataset_utils.train2000_PN_wo_NS",
        "func_name": "train2000_PN_wo_NS"},

    #Train100_Generated guidelines with both Positive and 15 Sibling examples:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_train_2000_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_examples/final_data_split/PA_100_dev_final.json
    "train2000_PS_w_NS": {
        "py_file": "dataset_utils.train2000_PS_w_NS",
        "func_name": "train2000_PS_w_NS"},
    "train2000_PS_wo_NS": {
        "py_file": "dataset_utils.train2000_PS_wo_NS",
        "func_name": "train2000_PS_wo_NS"}, 

    #Train100_Generated guidelines with consolidated random guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_adv_guidelines/final_data_split/PA_train_2000_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15random_adv_guidelines/final_data_split/PA_100_dev_final.json
    "train2000_PN_Adv_w_NExample": {
        "py_file": "dataset_utils.train2000_PN_Adv_w_NExample",
        "func_name": "train2000_PN_Adv_w_NExample"},
    "train2000_PN_Adv_wo_NExample": {
        "py_file": "dataset_utils.train2000_PN_Adv_wo_NExample",
        "func_name": "train2000_PN_Adv_wo_NExample"}, 

    #Train100_Generated guidelines with consolidated sibling guidelines:
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_adv_guidelines/final_data_split/PA_train_2000_w_neg.json
    # /scratch/spati/tmp/NLP_Research_Work/TextEE/data/guideline_experiments/ACE_15sibling_adv_guidelines/final_data_split/PA_100_dev_final.json
    "train2000_PS_Adv_w_NExample": {
        "py_file": "dataset_utils.train2000_PS_Adv_w_NExample",
        "func_name": "train2000_PS_Adv_w_NExample"},
    "train2000_PS_Adv_wo_NExample": {
        "py_file": "dataset_utils.train2000_PS_Adv_wo_NExample",
        "func_name": "train2000_PS_Adv_wo_NExample"}, 



    ############Inference the full GUIDELINE EXPERIMENTS on new_full_coverage_dev_set############
    #no_guidelines:
    "infer_wo_guidelines_w_NS": {
        "py_file": "dataset_utils.infer_wo_guidelines_w_NS",
        "func_name": "infer_wo_guidelines_w_NS"},
    "infer_wo_guidelines_wo_NS": {
        "py_file": "dataset_utils.infer_wo_guidelines_wo_NS",
        "func_name": "infer_wo_guidelines_wo_NS"},
    #human_guidelines:
    "infer_Human_w_NS": {
        "py_file": "dataset_utils.infer_Human_w_NS",
        "func_name": "infer_Human_w_NS"},
    "infer_Human_wo_NS": {
        "py_file": "dataset_utils.infer_Human_wo_NS",
        "func_name": "infer_Human_wo_NS"},
    #Generated guidelines with only Positive examples:
    "infer_guideline_P_w_NS": {
        "py_file": "dataset_utils.infer_guideline_P_w_NS",
        "func_name": "infer_guideline_P_w_NS"},
    "infer_guideline_P_wo_NS": {
        "py_file": "dataset_utils.infer_guideline_P_wo_NS",
        "func_name": "infer_guideline_P_wo_NS"},
    #Generated guidelines with both Positive and 15 Negative examples:
    "infer_guideline_PN_w_NS": {
        "py_file": "dataset_utils.infer_guideline_PN_w_NS",
        "func_name": "infer_guideline_PN_w_NS"},
    "infer_guideline_PN_wo_NS": {
        "py_file": "dataset_utils.infer_guideline_PN_wo_NS",
        "func_name": "infer_guideline_PN_wo_NS"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "infer_guideline_PS_w_NS": {
        "py_file": "dataset_utils.infer_guideline_PS_w_NS",
        "func_name": "infer_guideline_PS_w_NS"},
    "infer_guideline_PS_wo_NS": {
        "py_file": "dataset_utils.infer_guideline_PS_wo_NS",
        "func_name": "infer_guideline_PS_wo_NS"},
    #Generated guidelines consolidated:
    "infer_guideline_PN_Adv_wo_NS": {
        "py_file": "dataset_utils.infer_guideline_PN_Adv_wo_NS",
        "func_name": "infer_guideline_PN_Adv_wo_NS"},
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "infer_guideline_PN_Adv_w_NS" : {
        "py_file": "dataset_utils.infer_guideline_PN_Adv_w_NS",
        "func_name": "infer_guideline_PN_Adv_w_NS"},
    "infer_guideline_PS_Adv_wo_NS": {
        "py_file": "dataset_utils.infer_guideline_PS_Adv_wo_NS",
        "func_name": "infer_guideline_PS_Adv_wo_NS"},
    "infer_guideline_PS_Adv_w_NS" : {
        "py_file": "dataset_utils.infer_guideline_PS_Adv_w_NS",
        "func_name": "infer_guideline_PS_Adv_w_NS"},

    ############TEST on the full GUIDELINE EXPERIMENTS############
    #no_guidelines:
    "test_wo_guidelines_w_NS": {
        "py_file": "dataset_utils.test_wo_guidelines_w_NS",
        "func_name": "test_wo_guidelines_w_NS"},
    "test_wo_guidelines_wo_NS": {
        "py_file": "dataset_utils.test_wo_guidelines_wo_NS",
        "func_name": "test_wo_guidelines_wo_NS"},
    #human_guidelines:
    "test_Human_w_NS": {
        "py_file": "dataset_utils.test_Human_w_NS",
        "func_name": "test_Human_w_NS"},
    "test_Human_wo_NS": {
        "py_file": "dataset_utils.test_Human_wo_NS",
        "func_name": "test_Human_wo_NS"},
    #Generated guidelines with only Positive examples:
    "test_guideline_P_w_NS": {
        "py_file": "dataset_utils.test_guideline_P_w_NS",
        "func_name": "test_guideline_P_w_NS"},
    "test_guideline_P_wo_NS": {
        "py_file": "dataset_utils.test_guideline_P_wo_NS",
        "func_name": "test_guideline_P_wo_NS"},
    #Generated guidelines with both Positive and 15 Negative examples:
    "test_guideline_PN_w_NS": {
        "py_file": "dataset_utils.test_guideline_PN_w_NS",
        "func_name": "test_guideline_PN_w_NS"},
    "test_guideline_PN_wo_NS": {
        "py_file": "dataset_utils.test_guideline_PN_wo_NS",
        "func_name": "test_guideline_PN_wo_NS"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "test_guideline_PS_w_NS": {
        "py_file": "dataset_utils.test_guideline_PS_w_NS",
        "func_name": "test_guideline_PS_w_NS"},
    "test_guideline_PS_wo_NS": {
        "py_file": "dataset_utils.test_guideline_PS_wo_NS",
        "func_name": "test_guideline_PS_wo_NS"},
    #Generated guidelines consolidated:
    "test_guideline_PN_Adv_wo_NS": {
        "py_file": "dataset_utils.test_guideline_PN_Adv_wo_NS",
        "func_name": "test_guideline_PN_Adv_wo_NS"},
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "test_guideline_PN_Adv_w_NS" : {
        "py_file": "dataset_utils.test_guideline_PN_Adv_w_NS",
        "func_name": "test_guideline_PN_Adv_w_NS"},
    "test_guideline_PS_Adv_wo_NS": {
        "py_file": "dataset_utils.test_guideline_PS_Adv_wo_NS",
        "func_name": "test_guideline_PS_Adv_wo_NS"},
    "test_guideline_PS_Adv_w_NS" : {
        "py_file": "dataset_utils.test_guideline_PS_Adv_w_NS",
        "func_name": "test_guideline_PS_Adv_w_NS"},

    ############TEST on the 2000 GUIDELINE EXPERIMENTS############
    #no_guidelines:
    "test2000_wo_guidelines_w_NS": {
        "py_file": "dataset_utils.test2000_wo_guidelines_w_NS",
        "func_name": "test2000_wo_guidelines_w_NS"},
    "test2000_wo_guidelines_wo_NS": {
        "py_file": "dataset_utils.test2000_wo_guidelines_wo_NS",
        "func_name": "test2000_wo_guidelines_wo_NS"},
    #human_guidelines:
    "test2000_Human_w_NS": {
        "py_file": "dataset_utils.test2000_Human_w_NS",
        "func_name": "test2000_Human_w_NS"},
    "test2000_Human_wo_NS": {
        "py_file": "dataset_utils.test2000_Human_wo_NS",
        "func_name": "test2000_Human_wo_NS"},
    #Generated guidelines with only Positive examples:
    "test2000_P_w_NS": {
        "py_file": "dataset_utils.test2000_P_w_NS",
        "func_name": "test2000_P_w_NS"},
    "test2000_P_wo_NS": {
        "py_file": "dataset_utils.test2000_P_wo_NS",
        "func_name": "test2000_P_wo_NS"},
    #Generated guidelines with both Positive and 15 Negative examples:
    "test2000_PN_w_NS": {
        "py_file": "dataset_utils.test2000_PN_w_NS",
        "func_name": "test2000_PN_w_NS"},
    "test2000_PN_wo_NS": {
        "py_file": "dataset_utils.test2000_PN_wo_NS",
        "func_name": "test2000_PN_wo_NS"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "test2000_PS_w_NS": {
        "py_file": "dataset_utils.test2000_PS_w_NS",
        "func_name": "test2000_PS_w_NS"},
    "test2000_PS_wo_NS": {
        "py_file": "dataset_utils.test2000_PS_wo_NS",
        "func_name": "test2000_PS_wo_NS"},
    #Generated guidelines consolidated:
    "test2000_PN_Adv_wo_NS": {
        "py_file": "dataset_utils.test2000_PN_Adv_wo_NS",
        "func_name": "test2000_PN_Adv_wo_NS"},
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "test2000_PN_Adv_w_NS" : {
        "py_file": "dataset_utils.test2000_PN_Adv_w_NS",
        "func_name": "test2000_PN_Adv_w_NS"},
    "test2000_PS_Adv_wo_NS": {
        "py_file": "dataset_utils.test2000_PS_Adv_wo_NS",
        "func_name": "test2000_PS_Adv_wo_NS"},
    "test2000_PS_Adv_w_NS" : {
        "py_file": "dataset_utils.test2000_PS_Adv_w_NS",
        "func_name": "test2000_PS_Adv_w_NS"},
    
    
    
    
    #######################################################RICHERE#######################################################

    #RICHERE 100 training samples
    #gpu014
    "richere_train100_without_guideline_w_NS" : {
        "py_file": "dataset_utils.richere_train100_without_guideline_w_NS",
        "func_name": "richere_train100_without_guideline_w_NS"},
    #gpu012 - 0
    "richere_train100_without_guideline_wo_NS": {
        "py_file": "dataset_utils.richere_train100_without_guideline_wo_NS",
        "func_name": "richere_train100_without_guideline_wo_NS"},
    #gpu012 - 1
    "richere_train100_guidelineP_w_NS" : {
        "py_file": "dataset_utils.richere_train100_guidelineP_w_NS",
        "func_name": "richere_train100_guidelineP_w_NS"},
    "richere_train100_guidelineP_wo_NS": {
        "py_file": "dataset_utils.richere_train100_guidelineP_wo_NS",
        "func_name": "richere_train100_guidelineP_wo_NS"},
    "richere_train100_guidelinePN_w_NS" : {
        "py_file": "dataset_utils.richere_train100_guidelinePN_w_NS",
        "func_name": "richere_train100_guidelinePN_w_NS"},
    "richere_train100_guidelinePN_wo_NS": {
        "py_file": "dataset_utils.richere_train100_guidelinePN_wo_NS",
        "func_name": "richere_train100_guidelinePN_wo_NS"},
    "richere_train100_guidelinePS_w_NS" : {
        "py_file": "dataset_utils.richere_train100_guidelinePS_w_NS",
        "func_name": "richere_train100_guidelinePS_w_NS"},
    "richere_train100_guidelinePS_wo_NS": {
        "py_file": "dataset_utils.richere_train100_guidelinePS_wo_NS",
        "func_name": "richere_train100_guidelinePS_wo_NS"},
    "richere_train100_guidelinePN_Adv_w_NS" : {
        "py_file": "dataset_utils.richere_train100_guidelinePN_Adv_w_NS",
        "func_name": "richere_train100_guidelinePN_Adv_w_NS"},
    "richere_train100_guidelinePN_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_train100_guidelinePN_Adv_wo_NS",
        "func_name": "richere_train100_guidelinePN_Adv_wo_NS"},
    "richere_train100_guidelinePS_Adv_w_NS" : {
        "py_file": "dataset_utils.richere_train100_guidelinePS_Adv_w_NS",
        "func_name": "richere_train100_guidelinePS_Adv_w_NS"},
    "richere_train100_guidelinePS_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_train100_guidelinePS_Adv_wo_NS",
        "func_name": "richere_train100_guidelinePS_Adv_wo_NS"},

    #RICHERE 2000 training samples
    "richere_train2000_without_guideline_w_NS" : {
        "py_file": "dataset_utils.richere_train2000_without_guideline_w_NS",
        "func_name": "richere_train2000_without_guideline_w_NS"},
    "richere_train2000_without_guideline_wo_NS": {
        "py_file": "dataset_utils.richere_train2000_without_guideline_wo_NS",
        "func_name": "richere_train2000_without_guideline_wo_NS"},
    "richere_train2000_guidelineP_w_NS" : {
        "py_file": "dataset_utils.richere_train2000_guidelineP_w_NS",
        "func_name": "richere_train2000_guidelineP_w_NS"},
    "richere_train2000_guidelineP_wo_NS": {
        "py_file": "dataset_utils.richere_train2000_guidelineP_wo_NS",
        "func_name": "richere_train2000_guidelineP_wo_NS"},
    "richere_train2000_guidelinePN_w_NS" : {
        "py_file": "dataset_utils.richere_train2000_guidelinePN_w_NS",
        "func_name": "richere_train2000_guidelinePN_w_NS"},
    "richere_train2000_guidelinePN_wo_NS": {
        "py_file": "dataset_utils.richere_train2000_guidelinePN_wo_NS",
        "func_name": "richere_train2000_guidelinePN_wo_NS"},
    "richere_train2000_guidelinePS_w_NS" : {
        "py_file": "dataset_utils.richere_train2000_guidelinePS_w_NS",
        "func_name": "richere_train2000_guidelinePS_w_NS"},
    "richere_train2000_guidelinePS_wo_NS": {
        "py_file": "dataset_utils.richere_train2000_guidelinePS_wo_NS",
        "func_name": "richere_train2000_guidelinePS_wo_NS"},
    "richere_train2000_guidelinePN_Adv_w_NS" : {
        "py_file": "dataset_utils.richere_train2000_guidelinePN_Adv_w_NS",
        "func_name": "richere_train2000_guidelinePN_Adv_w_NS"},
    "richere_train2000_guidelinePN_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_train2000_guidelinePN_Adv_wo_NS",
        "func_name": "richere_train2000_guidelinePN_Adv_wo_NS"},
    "richere_train2000_guidelinePS_Adv_w_NS" : {
        "py_file": "dataset_utils.richere_train2000_guidelinePS_Adv_w_NS",
        "func_name": "richere_train2000_guidelinePS_Adv_w_NS"},
    "richere_train2000_guidelinePS_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_train2000_guidelinePS_Adv_wo_NS",
        "func_name": "richere_train2000_guidelinePS_Adv_wo_NS"},

    #RICHERE full training samples
    "richere_train_without_guideline_w_NS" : {
        "py_file": "dataset_utils.richere_train_without_guideline_w_NS",
        "func_name": "richere_train_without_guideline_w_NS"},
    "richere_train_without_guideline_wo_NS": {
        "py_file": "dataset_utils.richere_train_without_guideline_wo_NS",
        "func_name": "richere_train_without_guideline_wo_NS"},
    "richere_train_guidelineP_w_NS" : {
        "py_file": "dataset_utils.richere_train_guidelineP_w_NS",
        "func_name": "richere_train_guidelineP_w_NS"},
    "richere_train_guidelineP_wo_NS": {
        "py_file": "dataset_utils.richere_train_guidelineP_wo_NS",
        "func_name": "richere_train_guidelineP_wo_NS"},
    "richere_train_guidelinePN_w_NS" : {
        "py_file": "dataset_utils.richere_train_guidelinePN_w_NS",
        "func_name": "richere_train_guidelinePN_w_NS"},
    "richere_train_guidelinePN_wo_NS": {
        "py_file": "dataset_utils.richere_train_guidelinePN_wo_NS",
        "func_name": "richere_train_guidelinePN_wo_NS"},
    "richere_train_guidelinePS_w_NS" : {
        "py_file": "dataset_utils.richere_train_guidelinePS_w_NS",
        "func_name": "richere_train_guidelinePS_w_NS"},
    "richere_train_guidelinePS_wo_NS": {
        "py_file": "dataset_utils.richere_train_guidelinePS_wo_NS",
        "func_name": "richere_train_guidelinePS_wo_NS"},
    "richere_train_guidelinePN_Adv_w_NS" : {
        "py_file": "dataset_utils.richere_train_guidelinePN_Adv_w_NS",
        "func_name": "richere_train_guidelinePN_Adv_w_NS"},
    "richere_train_guidelinePN_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_train_guidelinePN_Adv_wo_NS",
        "func_name": "richere_train_guidelinePN_Adv_wo_NS"},
    "richere_train_guidelinePS_Adv_w_NS" : {
        "py_file": "dataset_utils.richere_train_guidelinePS_Adv_w_NS",
        "func_name": "richere_train_guidelinePS_Adv_w_NS"},
    "richere_train_guidelinePS_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_train_guidelinePS_Adv_wo_NS",
        "func_name": "richere_train_guidelinePS_Adv_wo_NS"},

    ############ACE: MINI_GUIDELINE EXPERIMENTS _ 2 different samplings############
    #Train100_no_guidelines:
    "miniguideline_train100_wo_guidelines_w_NS_iter1": {
        "py_file": "dataset_utils.miniguideline_train100_wo_guidelines_w_NS_iter1",
        "func_name": "miniguideline_train100_wo_guidelines_w_NS_iter1"},
    "miniguideline_train100_wo_guidelines_w_NS_iter2": {
        "py_file": "dataset_utils.miniguideline_train100_wo_guidelines_w_NS_iter2",
        "func_name": "miniguideline_train100_wo_guidelines_w_NS_iter2"},
    #Train100_human_guidelines:
    "miniguideline_train100_Human_w_NS_iter1": {
        "py_file": "dataset_utils.miniguideline_train100_Human_w_NS_iter1",
        "func_name": "miniguideline_train100_Human_w_NS_iter1"},
    "miniguideline_train100_Human_w_NS_iter2": {
        "py_file": "dataset_utils.miniguideline_train100_Human_w_NS_iter2",
        "func_name": "miniguideline_train100_Human_w_NS_iter2"},
    #Train100_Generated guidelines with only Positive examples:
    "miniguideline_train100_P_w_NS_iter1": {
        "py_file": "dataset_utils.miniguideline_train100_P_w_NS_iter1",
        "func_name": "miniguideline_train100_P_w_NS_iter1"},
    "miniguideline_train100_P_w_NS_iter2": {
        "py_file": "dataset_utils.miniguideline_train100_P_w_NS_iter2",
        "func_name": "miniguideline_train100_P_w_NS_iter2"},
    #Train100_Generated guidelines with both Positive and 15 Negative examples:
    "miniguideline_train100_PN_w_NS_iter1": {
        "py_file": "dataset_utils.miniguideline_train100_PN_w_NS_iter1",
        "func_name": "miniguideline_train100_PN_w_NS_iter1"},
    "miniguideline_train100_PN_w_NS_iter2": {
        "py_file": "dataset_utils.miniguideline_train100_PN_w_NS_iter2",
        "func_name": "miniguideline_train100_PN_w_NS_iter2"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "miniguideline_train100_PS_w_NS_iter1": {
        "py_file": "dataset_utils.miniguideline_train100_PS_w_NS_iter1",
        "func_name": "miniguideline_train100_PS_w_NS_iter1"},
    "miniguideline_train100_PS_w_NS_iter2": {
        "py_file": "dataset_utils.miniguideline_train100_PS_w_NS_iter2",
        "func_name": "miniguideline_train100_PS_w_NS_iter2"},
    #Train100_ consolidated adv random Generated guidelines:
    "miniguideline_train100_PN_Adv_w_NExample_iter1": {
        "py_file": "dataset_utils.miniguideline_train100_PN_Adv_w_NExample_iter1",
        "func_name": "miniguideline_train100_PN_Adv_w_NExample_iter1"},
    "miniguideline_train100_PN_Adv_w_NExample_iter2": {
        "py_file": "dataset_utils.miniguideline_train100_PN_Adv_w_NExample_iter2",
        "func_name": "miniguideline_train100_PN_Adv_w_NExample_iter2"}, 
    #Train100_ consolidated adv sibling Generated guidelines:
    "miniguideline_train100_PS_Adv_w_NExample_iter1": {
        "py_file": "dataset_utils.miniguideline_train100_PS_Adv_w_NExample_iter1",
        "func_name": "miniguideline_train100_PS_Adv_w_NExample_iter1"},
    "miniguideline_train100_PS_Adv_w_NExample_iter2": {
        "py_file": "dataset_utils.miniguideline_train100_PS_Adv_w_NExample_iter2",
        "func_name": "miniguideline_train100_PS_Adv_w_NExample_iter2"},

    ############ACE: test for 3 samples of Train100 for ACE############
    "test100_Human_w_NS_iter1": {
        "py_file": "dataset_utils.test100_Human_w_NS_iter1",
        "func_name": "test100_Human_w_NS_iter1"
    },
    "test100_Human_w_NS_iter2": {
        "py_file": "dataset_utils.test100_Human_w_NS_iter2",
        "func_name": "test100_Human_w_NS_iter2"
    },
    "test100_Human_w_NS": {
        "py_file": "dataset_utils.test100_Human_w_NS",
        "func_name": "test100_Human_w_NS"
    },
    "test100_P_w_NS_iter1": {
        "py_file": "dataset_utils.test100_P_w_NS_iter1",
        "func_name": "test100_P_w_NS_iter1"
    },
    "test100_P_w_NS_iter2": {
        "py_file": "dataset_utils.test100_P_w_NS_iter2",
        "func_name": "test100_P_w_NS_iter2"
    },
    "test100_P_w_NS": {
        "py_file": "dataset_utils.test100_P_w_NS",
        "func_name": "test100_P_w_NS"
    },
    "test100_PN_Adv_w_NS_iter1": {
        "py_file": "dataset_utils.test100_PN_Adv_w_NS_iter1",
        "func_name": "test100_PN_Adv_w_NS_iter1"
    },
    "test100_PN_Adv_w_NS_iter2": {
        "py_file": "dataset_utils.test100_PN_Adv_w_NS_iter2",
        "func_name": "test100_PN_Adv_w_NS_iter2"
    },
    "test100_PN_Adv_w_NS": {
        "py_file": "dataset_utils.test100_PN_Adv_w_NS",
        "func_name": "test100_PN_Adv_w_NS"
    },
    "test100_PN_w_NS_iter1": {
        "py_file": "dataset_utils.test100_PN_w_NS_iter1",
        "func_name": "test100_PN_w_NS_iter1"
    },
    "test100_PN_w_NS_iter2": {
        "py_file": "dataset_utils.test100_PN_w_NS_iter2",
        "func_name": "test100_PN_w_NS_iter2"
    },
    "test100_PN_w_NS": {
        "py_file": "dataset_utils.test100_PN_w_NS",
        "func_name": "test100_PN_w_NS"
    },
    "test100_PS_Adv_w_NS_iter1": {
        "py_file": "dataset_utils.test100_PS_Adv_w_NS_iter1",
        "func_name": "test100_PS_Adv_w_NS_iter1"
    },
    "test100_PS_Adv_w_NS_iter2": {
        "py_file": "dataset_utils.test100_PS_Adv_w_NS_iter2",
        "func_name": "test100_PS_Adv_w_NS_iter2"
    },
    "test100_PS_Adv_w_NS": {
        "py_file": "dataset_utils.test100_PS_Adv_w_NS",
        "func_name": "test100_PS_Adv_w_NS"
    },
    "test100_PS_w_NS_iter1": {
        "py_file": "dataset_utils.test100_PS_w_NS_iter1",
        "func_name": "test100_PS_w_NS_iter1"
    },
    "test100_PS_w_NS_iter2": {
        "py_file": "dataset_utils.test100_PS_w_NS_iter2",
        "func_name": "test100_PS_w_NS_iter2"
    },
    "test100_PS_w_NS": {
        "py_file": "dataset_utils.test100_PS_w_NS",
        "func_name": "test100_PS_w_NS"
    },
    "test100_wo_guidelines_w_NS_iter1": {
        "py_file": "dataset_utils.test100_wo_guidelines_w_NS_iter1",
        "func_name": "test100_wo_guidelines_w_NS_iter1"
    },
    "test100_wo_guidelines_w_NS_iter2": {
        "py_file": "dataset_utils.test100_wo_guidelines_w_NS_iter2",
        "func_name": "test100_wo_guidelines_w_NS_iter2"
    },
    "test100_wo_guidelines_w_NS": {
        "py_file": "dataset_utils.test100_wo_guidelines_w_NS",
        "func_name": "test100_wo_guidelines_w_NS"
    },

    ############RICHERE: Train 3 more samples of Train100############
    "richere_train100_guidelineP_w_NS_iter1": {
        "py_file": "dataset_utils.richere_train100_guidelineP_w_NS_iter1",
        "func_name": "richere_train100_guidelineP_w_NS_iter1"
    },
    "richere_train100_guidelineP_w_NS_iter2": {
        "py_file": "dataset_utils.richere_train100_guidelineP_w_NS_iter2",
        "func_name": "richere_train100_guidelineP_w_NS_iter2"
    },
    "richere_train100_guidelinePN_Adv_w_NS_iter1": {
        "py_file": "dataset_utils.richere_train100_guidelinePN_Adv_w_NS_iter1",
        "func_name": "richere_train100_guidelinePN_Adv_w_NS_iter1"
    },
    "richere_train100_guidelinePN_Adv_w_NS_iter2": {
        "py_file": "dataset_utils.richere_train100_guidelinePN_Adv_w_NS_iter2",
        "func_name": "richere_train100_guidelinePN_Adv_w_NS_iter2"
    },
    "richere_train100_guidelinePN_w_NS_iter1": {
        "py_file": "dataset_utils.richere_train100_guidelinePN_w_NS_iter1",
        "func_name": "richere_train100_guidelinePN_w_NS_iter1"
    },
    "richere_train100_guidelinePN_w_NS_iter2": {
        "py_file": "dataset_utils.richere_train100_guidelinePN_w_NS_iter2",
        "func_name": "richere_train100_guidelinePN_w_NS_iter2"
    },
    "richere_train100_guidelinePS_Adv_w_NS_iter1": {
        "py_file": "dataset_utils.richere_train100_guidelinePS_Adv_w_NS_iter1",
        "func_name": "richere_train100_guidelinePS_Adv_w_NS_iter1"
    },
    "richere_train100_guidelinePS_Adv_w_NS_iter2": {
        "py_file": "dataset_utils.richere_train100_guidelinePS_Adv_w_NS_iter2",
        "func_name": "richere_train100_guidelinePS_Adv_w_NS_iter2"
    },
    "richere_train100_guidelinePS_w_NS_iter1": {
        "py_file": "dataset_utils.richere_train100_guidelinePS_w_NS_iter1",
        "func_name": "richere_train100_guidelinePS_w_NS_iter1"
    },
    "richere_train100_guidelinePS_w_NS_iter2": {
        "py_file": "dataset_utils.richere_train100_guidelinePS_w_NS_iter2",
        "func_name": "richere_train100_guidelinePS_w_NS_iter2"
    },
    "richere_train100_without_guideline_w_NS_iter1": {
        "py_file": "dataset_utils.richere_train100_without_guideline_w_NS_iter1",
        "func_name": "richere_train100_without_guideline_w_NS_iter1"
    },
    "richere_train100_without_guideline_w_NS_iter2": {
        "py_file": "dataset_utils.richere_train100_without_guideline_w_NS_iter2",
        "func_name": "richere_train100_without_guideline_w_NS_iter2"
    },

    ############RICHERE: test for 3 samples of Train100############
    "richere_test100_guidelineP_w_NS_iter1": {
        "py_file": "dataset_utils.richere_test100_guidelineP_w_NS_iter1",
        "func_name": "richere_test100_guidelineP_w_NS_iter1"
    },
    "richere_test100_guidelineP_w_NS_iter2": {
        "py_file": "dataset_utils.richere_test100_guidelineP_w_NS_iter2",
        "func_name": "richere_test100_guidelineP_w_NS_iter2"
    },
    "richere_test100_guidelineP_w_NS": {
        "py_file": "dataset_utils.richere_test100_guidelineP_w_NS",
        "func_name": "richere_test100_guidelineP_w_NS"
    },
    "richere_test100_guidelineP_wo_NS": {
        "py_file": "dataset_utils.richere_test100_guidelineP_wo_NS",
        "func_name": "richere_test100_guidelineP_wo_NS"
    },
    "richere_test100_guidelinePN_Adv_w_NS_iter1": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_w_NS_iter1",
        "func_name": "richere_test100_guidelinePN_Adv_w_NS_iter1"
    },
    "richere_test100_guidelinePN_Adv_w_NS_iter2": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_w_NS_iter2",
        "func_name": "richere_test100_guidelinePN_Adv_w_NS_iter2"
    },
    "richere_test100_guidelinePN_Adv_w_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_w_NS",
        "func_name": "richere_test100_guidelinePN_Adv_w_NS"
    },
    "richere_test100_guidelinePN_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_Adv_wo_NS",
        "func_name": "richere_test100_guidelinePN_Adv_wo_NS"
    },
    "richere_test100_guidelinePN_w_NS_iter1": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_w_NS_iter1",
        "func_name": "richere_test100_guidelinePN_w_NS_iter1"
    },
    "richere_test100_guidelinePN_w_NS_iter2": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_w_NS_iter2",
        "func_name": "richere_test100_guidelinePN_w_NS_iter2"
    },
    "richere_test100_guidelinePN_w_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_w_NS",
        "func_name": "richere_test100_guidelinePN_w_NS"
    },
    "richere_test100_guidelinePN_wo_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePN_wo_NS",
        "func_name": "richere_test100_guidelinePN_wo_NS"
    },
    "richere_test100_guidelinePS_Adv_w_NS_iter1": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_w_NS_iter1",
        "func_name": "richere_test100_guidelinePS_Adv_w_NS_iter1"
    },
    "richere_test100_guidelinePS_Adv_w_NS_iter2": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_w_NS_iter2",
        "func_name": "richere_test100_guidelinePS_Adv_w_NS_iter2"
    },
    "richere_test100_guidelinePS_Adv_w_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_w_NS",
        "func_name": "richere_test100_guidelinePS_Adv_w_NS"
    },
    "richere_test100_guidelinePS_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_Adv_wo_NS",
        "func_name": "richere_test100_guidelinePS_Adv_wo_NS"
    },
    "richere_test100_guidelinePS_w_NS_iter1": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_w_NS_iter1",
        "func_name": "richere_test100_guidelinePS_w_NS_iter1"
    },
    "richere_test100_guidelinePS_w_NS_iter2": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_w_NS_iter2",
        "func_name": "richere_test100_guidelinePS_w_NS_iter2"
    },
    "richere_test100_guidelinePS_w_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_w_NS",
        "func_name": "richere_test100_guidelinePS_w_NS"
    },
    "richere_test100_guidelinePS_wo_NS": {
        "py_file": "dataset_utils.richere_test100_guidelinePS_wo_NS",
        "func_name": "richere_test100_guidelinePS_wo_NS"
    },
    "richere_test100_without_guideline_w_NS_iter1": {
        "py_file": "dataset_utils.richere_test100_without_guideline_w_NS_iter1",
        "func_name": "richere_test100_without_guideline_w_NS_iter1"
    },
    "richere_test100_without_guideline_w_NS_iter2": {
        "py_file": "dataset_utils.richere_test100_without_guideline_w_NS_iter2",
        "func_name": "richere_test100_without_guideline_w_NS_iter2"
    },
    "richere_test100_without_guideline_w_NS": {
        "py_file": "dataset_utils.richere_test100_without_guideline_w_NS",
        "func_name": "richere_test100_without_guideline_w_NS"
    },
    "richere_test100_without_guideline_wo_NS": {
        "py_file": "dataset_utils.richere_test100_without_guideline_wo_NS",
        "func_name": "richere_test100_without_guideline_wo_NS"
    },

    ############RICHERE: test for 2000 Train############
    "richere_test2000_guidelineP_w_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelineP_w_NS",
        "func_name": "richere_test2000_guidelineP_w_NS"
    },
    "richere_test2000_guidelineP_wo_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelineP_wo_NS",
        "func_name": "richere_test2000_guidelineP_wo_NS"
    },
    "richere_test2000_guidelinePN_Adv_w_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePN_Adv_w_NS",
        "func_name": "richere_test2000_guidelinePN_Adv_w_NS"
    },
    "richere_test2000_guidelinePN_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePN_Adv_wo_NS",
        "func_name": "richere_test2000_guidelinePN_Adv_wo_NS"
    },
    "richere_test2000_guidelinePN_w_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePN_w_NS",
        "func_name": "richere_test2000_guidelinePN_w_NS"
    },
    "richere_test2000_guidelinePN_wo_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePN_wo_NS",
        "func_name": "richere_test2000_guidelinePN_wo_NS"
    },
    "richere_test2000_guidelinePS_Adv_w_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePS_Adv_w_NS",
        "func_name": "richere_test2000_guidelinePS_Adv_w_NS"
    },
    "richere_test2000_guidelinePS_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePS_Adv_wo_NS",
        "func_name": "richere_test2000_guidelinePS_Adv_wo_NS"
    },
    "richere_test2000_guidelinePS_w_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePS_w_NS",
        "func_name": "richere_test2000_guidelinePS_w_NS"
    },
    "richere_test2000_guidelinePS_wo_NS": {
        "py_file": "dataset_utils.richere_test2000_guidelinePS_wo_NS",
        "func_name": "richere_test2000_guidelinePS_wo_NS"
    },
    "richere_test2000_without_guideline_w_NS": {
        "py_file": "dataset_utils.richere_test2000_without_guideline_w_NS",
        "func_name": "richere_test2000_without_guideline_w_NS"
    },
    "richere_test2000_without_guideline_wo_NS": {
        "py_file": "dataset_utils.richere_test2000_without_guideline_wo_NS",
        "func_name": "richere_test2000_without_guideline_wo_NS"
    },

    ############RICHERE: test for full Train############
    "richere_test_guidelineP_w_NS": {
        "py_file": "dataset_utils.richere_test_guidelineP_w_NS",
        "func_name": "richere_test_guidelineP_w_NS"
    },
    "richere_test_guidelineP_wo_NS": {
        "py_file": "dataset_utils.richere_test_guidelineP_wo_NS",
        "func_name": "richere_test_guidelineP_wo_NS"
    },
    "richere_test_guidelinePN_Adv_w_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePN_Adv_w_NS",
        "func_name": "richere_test_guidelinePN_Adv_w_NS"
    },
    "richere_test_guidelinePN_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePN_Adv_wo_NS",
        "func_name": "richere_test_guidelinePN_Adv_wo_NS"
    },
    "richere_test_guidelinePN_w_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePN_w_NS",
        "func_name": "richere_test_guidelinePN_w_NS"
    },
    "richere_test_guidelinePN_wo_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePN_wo_NS",
        "func_name": "richere_test_guidelinePN_wo_NS"
    },
    "richere_test_guidelinePS_Adv_w_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePS_Adv_w_NS",
        "func_name": "richere_test_guidelinePS_Adv_w_NS"
    },
    "richere_test_guidelinePS_Adv_wo_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePS_Adv_wo_NS",
        "func_name": "richere_test_guidelinePS_Adv_wo_NS"
    },
    "richere_test_guidelinePS_w_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePS_w_NS",
        "func_name": "richere_test_guidelinePS_w_NS"
    },
    "richere_test_guidelinePS_wo_NS": {
        "py_file": "dataset_utils.richere_test_guidelinePS_wo_NS",
        "func_name": "richere_test_guidelinePS_wo_NS"
    },
    "richere_test_without_guideline_w_NS": {
        "py_file": "dataset_utils.richere_test_without_guideline_w_NS",
        "func_name": "richere_test_without_guideline_w_NS"
    },
    "richere_test_without_guideline_wo_NS": {
        "py_file": "dataset_utils.richere_test_without_guideline_wo_NS",
        "func_name": "richere_test_without_guideline_wo_NS"
    },
    
    ############FULL RICHERE TRAIN-> FULL TEST RICHERE, Test on the full ACE Test Data GUIDELINE EXPERIMENTS, Trained on full RICHERE Train Data############
    #no_guidelines:
    "test_wo_guidelines_w_NS_richeretrained": {
        "py_file": "dataset_utils.test_wo_guidelines_w_NS_richeretrained",
        "func_name": "test_wo_guidelines_w_NS_richeretrained"},
    "test_wo_guidelines_wo_NS_richeretrained": {
        "py_file": "dataset_utils.test_wo_guidelines_wo_NS_richeretrained",
        "func_name": "test_wo_guidelines_wo_NS_richeretrained"},
    #human_guidelines:
    "test_Human_w_NS_richeretrained": {
        "py_file": "dataset_utils.test_Human_w_NS_richeretrained",
        "func_name": "test_Human_w_NS_richeretrained"},
    "test_Human_wo_NS_richeretrained": {
        "py_file": "dataset_utils.test_Human_wo_NS_richeretrained",
        "func_name": "test_Human_wo_NS_richeretrained"},
    #Generated guidelines with only Positive examples:
    "test_guideline_P_w_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_P_w_NS_richeretrained",
        "func_name": "test_guideline_P_w_NS_richeretrained"},
    "test_guideline_P_wo_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_P_wo_NS_richeretrained",
        "func_name": "test_guideline_P_wo_NS_richeretrained"},
    #Generated guidelines with both Positive and 15 Negative examples:
    "test_guideline_PN_w_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_PN_w_NS_richeretrained",
        "func_name": "test_guideline_PN_w_NS_richeretrained"},
    "test_guideline_PN_wo_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_PN_wo_NS_richeretrained",
        "func_name": "test_guideline_PN_wo_NS_richeretrained"},
    #Generated guidelines with both Positive and 15 Sibling examples:
    "test_guideline_PS_w_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_PS_w_NS_richeretrained",
        "func_name": "test_guideline_PS_w_NS_richeretrained"},
    "test_guideline_PS_wo_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_PS_wo_NS_richeretrained",
        "func_name": "test_guideline_PS_wo_NS_richeretrained"},
    #Generated guidelines consolidated:
    "test_guideline_PN_Adv_wo_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_PN_Adv_wo_NS_richeretrained",
        "func_name": "test_guideline_PN_Adv_wo_NS_richeretrained"},
    #from here below were trained on total train - checkpointed on full coverage dev set hence, infered on old dev set without full coverage.
    "test_guideline_PN_Adv_w_NS_richeretrained" : {
        "py_file": "dataset_utils.test_guideline_PN_Adv_w_NS_richeretrained",
        "func_name": "test_guideline_PN_Adv_w_NS_richeretrained"},
    "test_guideline_PS_Adv_wo_NS_richeretrained": {
        "py_file": "dataset_utils.test_guideline_PS_Adv_wo_NS_richeretrained",
        "func_name": "test_guideline_PS_Adv_wo_NS_richeretrained"},
    "test_guideline_PS_Adv_w_NS_richeretrained" : {
        "py_file": "dataset_utils.test_guideline_PS_Adv_w_NS_richeretrained",
        "func_name": "test_guideline_PS_Adv_w_NS_richeretrained"},
}

def load_dataset(dataset_name):
    # print(dataset_mapper, dataset_name)
    dataset_info = dataset_mapper.get(dataset_name)
    
    if dataset_info:
        module_name = dataset_info["py_file"]  # Get the module (Python file) as a string
        func_name = dataset_info["func_name"]  # Get the function name as a string
        
        # Dynamically import the module using importlib
        module = importlib.import_module(module_name)
        
        # Get the function from the module
        func = getattr(module, func_name)
        
        # Call the function
        return func()  # Assuming the function takes no arguments
    else:
        raise ValueError(f"Dataset {dataset_name} not found in dataset_mapper.")
