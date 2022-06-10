package packt.comet;

import ml.comet.experiment.ExperimentBuilder;
import ml.comet.experiment.OnlineExperiment;
import weka.core.Instances;
import weka.core.converters.CSVLoader;
import weka.classifiers.Classifier;
import weka.classifiers.lazy.IBk;
import weka.classifiers.Evaluation;
import java.util.Random;
import java.io.File;



public class KNN 
{
    
    public static void main( String[] args )
    {
        
        OnlineExperiment experiment = ExperimentBuilder.OnlineExperiment()
                        .build();
        experiment.setExperimentName("KNN");
        
        try {
            CSVLoader loader = new CSVLoader();
            loader.setSource(new File("src/main/resources/mushrooms.csv"));
            
            Instances data = loader.getDataSet();
            data.setClassIndex(0);

            

            int n = data.numInstances();
            for (int i = 200; i < n+1000; i+=1000) {
                if(i > n)
                    i = n;
                Instances current_data = new Instances(data, 0, i);
                
                // train test splitting
                int seed = 10;
                current_data.randomize(new Random(seed));
                int trainSize = (int) Math.round(current_data.numInstances() * 0.7);
                int testSize = current_data.numInstances() - trainSize;
                
                Instances train = new Instances(current_data, 0, trainSize);
                Instances test = new Instances(current_data, trainSize, testSize);

                // train the model
                IBk model = new IBk();	
                model.buildClassifier(train);

                // evaluate the model
                Evaluation eval = new Evaluation(test);
                eval.evaluateModel(model,test);

                double accuracy = eval.pctCorrect()/100;
                
                experiment.logMetric("accuracy", accuracy);
                experiment.setStep(i);
            }   
        } catch (Exception ex) {
			System.err.println("Exception occurred! " + ex);
		}
        experiment.end();
    }
}
