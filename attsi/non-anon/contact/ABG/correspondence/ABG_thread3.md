<!-- PII: Raw Discord capture. Contains Discord handles, research interests,
     and external links voluntarily posted by ABG members in the
     #project-proposals channel. Internal reference only — do not redistribute.
     See ABG_ANALYSIS.md for structured summary. -->

This is the start of the #project-proposals channel.
bake3011 — 5/2/2026 9:53 PM
One of the cool project I can think of is to use AlphaFold to modeling large protein structure (>2k aa). Not sure what the target will be but I think it can be a fun side project
rosīe — 5/2/2026 11:21 PM
this is also interesting but please write more if you still want to propose this
bake3011 — 5/2/2026 11:22 PM
Ok. I need to double check on it. Just throwing idea out for now
Alistaire — Yesterday at 3:47 PM
If a protein can be split up into separate domains, you can do this for those domains easily, so either you could do those low hanging fruit or consider focusing on cases where it doesn't work? SWISSMODEL has an input limit of 5000 residues
bake3011 — Yesterday at 9:17 PM
Honestly, I think we should just start with those low hanging fruit. The server just starts so probably starting with some smaller sized projects and then we move bigger would work better
Everybody here are still trying to figure out how things work after al


Jeremy — 5/2/2026 11:15 PM
Project proposal: Single-cell meta-analysis identifies recurrence-associated tumor and macrophage programs in pediatric ependymoma

Hypothesis: Ependymoma recurrence and poor outcome are associated with a conserved shift toward undifferentiated/progenitor-like, mesenchymal/hypoxic, and macrophage-enriched programs detectable across public single-cell datasets and validated in bulk transcriptomic cohorts.

Datasets: GSE141460, GSE125969, GSE163686 (validation: GSE226961

Background (ChatGPT wrote this summary from a few PDFs I sent it): Ependymoma is a primary CNS tumor with clinically important molecular subgroups. Posterior fossa group A, or PFA, is especially relevant because it is associated with worse outcomes and frequent relapse. A 2024 Acta Neuropathologica study notes that PFA ependymoma is the most common and aggressive pediatric ependymoma subtype, and it analyzed primary and relapse samples to study recurrence biology.

The opportunity is that ependymoma already has public single-cell datasets, but the field is not as crowded as GBM. Existing studies often focus on one cohort, one anatomical group, or one biological story. A clean cross-public-dataset integration + bulk outcome validation paper could still be plausible.

What this would take: Google collab Pro or Pro+

Methodology (so far, this is just basic scseq): Download and keep datasets in collab, filter datasets, normalize data (batch effects), annotate cell types, focus on program familes, derive signatures, validate, do microneviroment analysis, make figures
rosīe — 5/2/2026 11:20 PM
this is appealing but i'd caution against the use of chatgpt to analyze background. i'll look through the methodology here but it does look promising. don't start writing the full plan yet
oh also don't write so much. target is like 2-3 paragraphs
bake3011 — 5/2/2026 11:22 PM
If you share a google doc, I think we can just pop some stuffs in or how you want it to work?
rosīe — 5/2/2026 11:25 PM
hmmm yeah a google doc could work for a project plan. anything i can look over. like i said don't start yet since i still need to check the proposal but looks good as of now. 

either you or @Jeremy make one and make sure the link is public so everyone can see it
LinearParadox — 5/3/2026 9:55 PM
how are you defining programs here is the main thing imo
Jeremy — Yesterday at 12:12 AM
wdym programs
LinearParadox — Yesterday at 1:20 AM
You say focus on program families and derive signatures
Jeremy — Yesterday at 2:24 PM
ohh
i mean like just look for signatures of things on the DGE level
so like for example run DGE then in each set we group genes into things like neuroinflammation, neutrophil activation, etc
for signatures we can use predefined sets from GO sites and score each with GVSA
rosīe — Yesterday at 10:00 PM
assuming you mean GSVA here
Jeremy — 12:36 AM
yes mb




Jeremy — 5/3/2026 10:35 AM
Another proposal (GPT 5.5 helped with researching background and finding related studies): 

Research question: Do hidradenitis suppurativa and Crohn's disease share reproducible IL-17/TNF/neutrophil-associated transcriptomic programs across public bulk datasets?

Background: Crohn's disease is a chronic, relapsing inflammatory bowel disease in which immune dysregulation damages segments of the gastrointestinal tract, often producing abdominal pain, diarrhea, bleeding, strictures, fistulas, and systemic inflammation. Hidradenitis suppurativa is a chronic inflammatory skin disease centered on hair follicles, usually affecting intertriginous areas such as the axillae, groin, perineal region, and inframammary folds, with recurrent painful nodules, abscesses, draining tunnels, and scarring. The two diseases are linked: patients with HS have increased odds of Crohn's disease, and both disorders show overlapping immune biology, especially TNF-α, IL-23/Th17 signaling, neutrophil recruitment, macrophage activation, epithelial/barrier dysfunction, microbial dysbiosis, and chronic tissue-remodeling inflammation. 

Methodology: 
Collect 2-4 HS datasets and 2-4 Crohn's datasets.
Analyze each dataset separately with  DESeq2.
Use FDR correction.
Identify replicated disease DEGs within each disease.
Intersect same-direction replicated genes.
Run GO/Reactome/KEGG and full-ranked GSEA.
Add immune-cell deconvolution.
Prioritize genes by replication, effect size, pathway relevance, and PPI only as secondary support.
Validate top genes/signature in independent datasets.
Make clean figures and release code.

Related studies: 
For clinical/epidemiologic justification of the HS-IBD link: DOI: 10.1001/jamadermatol.2019.0891.
Useful recent evidence that the association is bidirectional: DOI: 10.2340/actadv.v105.43657.
Good background review on shared clinical and mechanistic links: DOI: 10.3390/biomedicines13081833.
Jeremy — 5/3/2026 10:38 AM
longer writeup: https://docs.google.com/document/d/1nkHwxg2-p3ZbuQjTaFtQdhGjeG8Db2CaF1m2A_grh84/edit?tab=t.0

This isn't scseq. We'd be doing a standard DEG comparison of two connected diseases that have rarely been compared in the gene expression context
Google Docs
Project: DEG analysis of HS and Crohn's disease
Research question: Do hidradenitis suppurativa and Crohn's disease share reproducible IL-17/TNF/neutrophil-associated transcriptomic programs across public bulk datasets?Background: Crohn's disease is a chronic, relapsing inflammatory bowel disease in which immune dysregulation damages segments...
Image
rosīe — 5/3/2026 11:26 AM
appealing and well written. it seems like it could be done fast and effectively with the right guidance and mentorship. skeptical of the claim that it hasn't been done already though
LinearParadox — 5/3/2026 9:59 PM
don't single cell datasets exist for both of these
Like singe cell seems like a somewhat superior way of examining this
Tiptop10 — Yesterday at 11:47 AM
For this project you could merge the DEG results based on the cohen's d (based of the SMD and variance of the SMD). To pool the disease datasets from different studies' deconvoluted celltypes, since you should take into account that experiments can yield different types of sizes of variation.

And then just perform the analysis methods on the pooled disease datasets. To make it easier to analyze. And then just for example quadrant plots between the celltype expression levels of the diseases. Correct me if I'm wrong 
LinearParadox — Yesterday at 2:08 PM
you're performing DGE prior to deconvolution, no? further i wouldn't really trust any sort of differential expression on deconvoluted data. (You don't know how well you're de convoluting, you're probably violating some deseq assumptions atp). Also why Cohens d? Just use the shrunken LFC
Tiptop10 — Yesterday at 2:20 PM
Ah it seems I have confused some terms, looking back it doesn't really make sense no, thanks for the corrections
Jeremy — Yesterday at 2:49 PM
pardon my ignorance but why would scseq be inherently better
LinearParadox — Yesterday at 2:50 PM
You're trying to do immune cell deconvolution
why do immune cell deconvolution when you have a direct measure of immune cell abundances with transcriptomics
Jeremy — Yesterday at 2:50 PM
ohhh
yeah that makes sense sorry
LinearParadox — Yesterday at 2:51 PM
also you're examining different tissues, it would be helpful for the head to head comparison as you can narrow down immune cell types for comparisons rather than comparing the bulk tissue, which in theory should be more comparable 
Jeremy — Yesterday at 2:56 PM
ok tysm sorry for my ignorance
i'll update the proposal



Mark — Yesterday at 4:16 PM
Background on why this proposal in particular. My lab works on protein tyrosine phosphatases, enzymes that regulate cellular protein phosphorylations. We're working on a specific one, funded by the NIH, that is involved in metastasis. There are other PTPs that have been linked to metastasis, so we're interested in looking at published data sets for evidence of PTPs being expressed in (or maybe overexpressed) in metastases or agressive cancers.

I think this would be a relatively small project at first. We're going to need to look for relevant datasets and define the question. There's 100+ PTPs, so maybe look at all expression in a few cancers, or can also choose a few and look at their expression in a broader selection of cancer types/sub-types. 

My timeline for this is probably a semester to a year, although someone who is adept at analysis of transcriptomics data would probably be able to analyze pretty fast.
rosīe — Yesterday at 6:17 PM
This is a great idea. I would only choose a few representative cancers / types like you said, especially those where metastasis/aggressiveness datasets are strong (then screen the PTP family within those contexts). I'm especially confident that this project could do well given that you have apparent lab experience in this exact field.

I honestly think this could be done with a shorter timeline if you have a lot of collaborators and parallelize work as much as possible. 

One possible tool for initial screening is TNMplot: https://pubmed.ncbi.nlm.nih.gov/33807717/




Mark — Yesterday at 4:26 PM
MD simulation of membrane protein involved in drug resistance

Chloroquine resistance in Plasmodium falciparumis attributed to mutations in a transporter called PfCRT, (known structure). A second transporter, AAT1, was also identified that confers resistance (https://www.nature.com/articles/s41564-023-01377-z). Mutations have been identified in AAT1 that contributes to both resistance and fitness of the organism. No structure is available for PfAAT1. The study did generate models, but no further analysis was done structurally.

Project is 100% computation for now. Need to model structure and simulations to see effect of mutations on structure and/or dynamics. CRT structure is available so that can be used as a basis. Involves docking and molecular dynamics simulations.

Deliverable would be some proposed molecular mechanism for the transporter's ability to confer resistance and fitness to P. falciparum. It's essentially a hypothesis that links molecular level to organism, and since there's population data available, directly relates to some real-world impact.
LinearParadox — Yesterday at 4:46 PM
not a huge protein guy but one problem ppl should be aware of is that the AAT1 AF structure is quite poor
Alistaire — Yesterday at 4:47 PM
I've done molecular docking studies of membrane proteins before, and got good results for finding which interaction correlates with an experimental response. Got maybe a nice setup to run something already

You'd definitely want MD for sure to really validate, I have less experience with it though
Mark — Yesterday at 4:48 PM
that is true. Going to require lots of validation. Can always extend this to wet lab 🤷‍♂️
haven't really dug deep into it. I added a seminar and they showed that and I'm like, why didn't you... It's not going to be a high-impact paper to do it all computationally, but might show some interesting hypothesis to build on later
Alistaire — Yesterday at 4:50 PM
I feel like known genetic variance is already good enough experimental data, but I mean validating the vacuum docking result not falling apart immediately in MD 😛
Mark — Yesterday at 4:52 PM
that's what i was thinking about. it's not functional correlation (mutation 1 leads to increased transport) but at the population level they see trends in drug resistance. So the Dock/MD would be a first attempt to bridge that until we get more experimental data. 

Ig could address the poor AF structure by looking at homologous proteins or proteins of the same fold. If anyone's interested, I'll deep dive more after I submit grades this semester 😂
LinearParadox — Yesterday at 4:52 PM
don't you need a starting structure for MD?
Mark — Yesterday at 4:52 PM
you do and it's going to have to be a model in this case
LinearParadox — Yesterday at 4:52 PM
doesn't alpha fold kind of do this internally (at least doing the MSA)
Alistaire — Yesterday at 4:53 PM
Swiss-model and modbase could have better models for the dockable parts
Mark — Yesterday at 4:54 PM
it does, so first thing to look at is how rich is the MSA? Paper used AF and I-TASSER. I don't remember how they validated the models.
LinearParadox — Yesterday at 4:54 PM
🙁
Image
LinearParadox — Yesterday at 4:55 PM
i mean it uses the whole uniprot database by default. you could probs quickly build a rough version with mmseqs2
Mark — Yesterday at 4:57 PM
that disordered N-terminal and the helix that's sticking sideways. prob not as trivial as i originally thought
Image
Alistaire — Yesterday at 5:07 PM
I'm assuming it's either IDR or retrying with just that part will fold it fine.. let's see
Alistaire — Yesterday at 5:38 PM
>Models were truncated to exclude amino-terminal residues 1–166, probably positioned outside of the membrane, because AlphaFold assigns low confidence to this N-terminal stretch. Furthermore, mutations of interest map only to transmembrane helices according to both 3D models and TOPCONS.
rosīe — Yesterday at 6:20 PM
This idea is really great and definitely very novel, though it would be harder to do (at least to do right/rigorously). I'm a big fan of both of the ones you sent, however.



bake3011 — 1:04 AM
Objective
This project will evaluate whether gene expression profiles from publicly available RNA-seq datasets can predict TMS scores and identify candidate biomarkers associated with TMS variation.

Approach
We will collect matched RNA-seq expression data and TMS scores from GEO database. RNA-seq data will be normalized and filtered to retain genes with sufficient expression and variance across samples. Linear regression models will then be used to test associations between individual gene expression levels and TMS scores.

For biomarker discovery, each gene will first be evaluated using univariate linear regression, with TMS score as the dependent variable and normalized gene expression as the predictor. Multiple-testing correction will be applied to control the false discovery rate. Top candidate genes will then be assessed in multivariable regression models, potentially including clinical covariates such as age, sex, disease subtype, or treatment status where available.

Deliverables
The analysis will produce a ranked list of genes associated with TMS score, regression coefficients, confidence intervals, adjusted p-values, and model performance metrics. Selected biomarkers will be visualized using scatter plots, heatmaps, and pathway enrichment analysis to support biological interpretation.

Expected Outcome
This study will identify RNA-seq-derived biomarkers that correlate with TMS scores and may help predict disease state, therapeutic response, or biological mechanisms underlying TMS variation. The results can guide future validation studies using independent cohorts or targeted assays such as qPCR.

Note: This is generated by chatGPT but the idea remains the same. Relatively small project, suitable for probably group of 4-6 people, 3-6months. This is the original research that I based on https://doi.org/10.1038/ejhg.2014.281. They used SE tag based sequencing so I hope by doing RNA-seq, we would have much better/accurate results 
LinearParadox — 1:08 AM
anyone can make a thread
bake3011 — 1:08 AM
oh did not know that
I think ai would explain it better than I do
Image
but essentially higher the score, the worse the disease
essentially we are making a link between phenotypic and transcriptomic data
LinearParadox — 1:10 AM
will say as an addon you should do something like LASSO bc you will have a ton of genes / features
bake3011 — 1:12 AM
Potentially, I mean I'm down to modifying the methods if it makes sense.
I don't think this project will be too hard and perfect for a new group like us to test the water. I don't want to jump to a big project without any big certainty that it will be done. Instead, this project can act as a proof of concept/case study for the server. Once we get a publication out of this, we can move on a bigger project ans so forth.
bake3011 — 1:36 AM
https://docs.google.com/document/d/1ATYNJsjYk9C5B_S6Va6q8UQprGsY4TjTuDpYTkAAzlk/edit?usp=sharing
